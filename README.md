# YouTube Transcript API (Vercel)

Bu klasör, YouTube transkriptlerini çeken Python kodunu Vercel üzerinde ücretsiz barındırmak için hazırlanmıştır.

## Nasıl Yüklenir?

1. **GitHub'a Yükle:**
   - Bu klasörün içeriğini (`api`, `requirements.txt`, `vercel.json` vb.) GitHub'da yeni bir repo olarak oluşturun.

2. **Vercel'e Bağla:**
   - [Vercel Dashboard](https://vercel.com/dashboard) adresine gidin.
   - "Add New Project" deyin.
   - GitHub reponuzu seçin ("Import").
   - **Framework Preset:** "Other" olarak kalsın (Otomatik Python algılar).
   - "Deploy" butonuna basın.

3. **URL'i Alın:**
   - Deploy bitince `https://proje-adiniz.vercel.app` gibi bir link verecek.
   - API Linkiniz: `https://proje-adiniz.vercel.app/api/transcript?v=VIDEO_ID`

## Kullanım Örneği

```
https://sizin-projeniz.vercel.app/api/transcript?v=6CFCX2LmcKI
```
