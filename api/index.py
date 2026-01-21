from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)
CORS(app)

def extract_video_id(url_or_id):
    if len(url_or_id) == 11 and re.match(r'^[a-zA-Z0-9_-]+$', url_or_id):
        return url_or_id
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'[?&]v=([a-zA-Z0-9_-]{11})'
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return None

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == "":
        return jsonify({
            "status": "ok",
            "usage": "GET /api/transcript?v=VIDEO_ID",
            "platform": "vercel"
        })
    return jsonify({"error": "Not found"}), 404

@app.route('/api/transcript')
def get_transcript():
    video_input = request.args.get('v', '')
    if not video_input:
        return jsonify({"success": False, "error": "Video ID veya URL gerekli"}), 400
    
    video_id = extract_video_id(video_input)
    if not video_id:
        return jsonify({"success": False, "error": "Geçersiz ID"}), 400
    
    try:
        # GÜNCELLEME: Yeni API (v1.x) kullanımı
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr', 'en']) 
        # NOT: Eğer v0.6 ise bu çalışır, v1.2 ise hata verir.
        # İkisini de deneyelim:
        
        return jsonify({
            "success": True,
            "video_id": video_id,
            "transcript": transcript_list
        })
    except AttributeError:
        # Yeni versiyon (v1.x) için fallback
        try:
            transcript = YouTubeTranscriptApi().fetch(video_id, languages=['tr', 'en'])
            # FetchedTranscript objesini listeye çevir
            if hasattr(transcript, 'to_raw_data'):
                raw_data = transcript.to_raw_data()
            else:
                raw_data = list(transcript)
                
            return jsonify({
                "success": True,
                "video_id": video_id,
                "transcript": raw_data
            })
        except Exception as e2:
             return jsonify({"success": False, "error": str(e2)}), 500
             
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
