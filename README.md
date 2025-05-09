### Proyek Akhir: Menyelesaikan Permasalahan Dropout Mahasiswa Wi Wok De Tok Institut ###
### Business Understanding ###
Wi Wok De Tok Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusu.

## Permasalahan Bisnis ##
Wi Wok De Tok Institut kesulitan mendeteksi kemungkinan mahasiswa dropout dan memonitor performa mahasiswa yang berkuliah di Wi WokmDe Tok Institut. Serta memberikan recomendation action kepada petinggi yang bersangkutan untuk menyelesaikan permasalahan tingginya angka dropout pada We Wok De Tok Institut.

## Cakupan Proyek ##
- Menganalisis data performa mahasiswa dan mencari penyebab dropout.
- Membuat dashboard performa mahasiswa untuk menampilkan statistik terkait dropout dan memberikan wawasan yang lebih baik.
- Menyediakan rekomendasi berbasis machine learning untuk mengurangi tingkat dropout.

### Persiapan ###
Sumber data: [Students' Performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Setup environment: 
```bash
# Install virtual env in vscode
python -m venv deployment

# Active virtual env
.\deployment\Scripts\activate

# Install necessary packages
pip install -r requirements.txt

# Run streamlit
streamlit run app.py
```
## Business Dashboard ##
Link Student Performance Dashboard  : [Student's Performance Dashboad](https://public.tableau.com/app/profile/rifki.nova.suryo/viz/StudentsPerformanceDashboard_17467529276790/Dashboard1?publish=yes) 

![rifki_suryo-Dashboard](https://github.com/user-attachments/assets/aa59f9b4-2c5d-4344-9e52-add25b421b62)


Pada dashboard di atas berisikan berbagai visualisasi yang mencakup total student's, dropout rate, dropout count, graduate count, student's status, dropout by martial status, dropout by gender dan mata kuliah yang memiliki dropout rate teringgi. Dashboard ini berfungsi sebagai alat bagi We Wi De Tok Institut khususnya dibagian akademik untuk memonitor performa mahasiswa dan mahasiswi yang berkuliah di sana.

## Menjalankan Sistem Machine Learning ##
Untuk menjalankan machine learning prototype, ikuti langkah berikut:
```bash
# Clone the repository
git clone <repository-url>

# Install necessary packages
pip install -r requiments.txt

# Run streamlit
streamlit run app.py
```
Berikut adalah link machine learning prototype: [Student Dropout Prediction]()

## Conclusion ##
Dashboard ini menampilkan berbagai visualisasi terkait performa mahasiswa dengan fokus pada analisis dropout. Tingginya angka dropout sebesar 39.1% dari total 4.424 mahasiswa mengindikasikan masalah serius yang perlu ditangani. Berdasarkan visualisasi, dropout tertinggi terjadi pada mahasiswa berjenis kelamin perempuan dengan 720 mahasiswa sedangkan pada mahasiswa berjenis kelamin laki-laki 701 mahasiswa yang melakukan dropout, sedangkan dari status pernikahan, mahasiswa single menyumbang dropout tertinggi 1184 kasua. Dropout juga paling banyak terjadi di program studi seperti Management (kelas malam) , Management reguler,  Nursing dan journalism and communication yang masing-masing mencatat lebih dari 100 kasus.

## Rekomendasi Action Items ##
Setelah membuat dashboard dan machine learning berikut beberapa rekomendasi action untuk We Wok De Tok Institut agar meningkatkan lulusan dengan reputasi yang baik:
 1. Melakukan bimbingan akademik dan konsultasi psikologis cara ini dapat difokuskan dan ditarget kepada semua mahasiswa yang memiliki indikasi akan melakukan dropout seperti mahasiswa yang masih single atau lajang yang berasal dari jurusan yang memiliki tingkat dropout tertinggi.
 2. Melakukan evaluasi pada jurusan yang memiliki kasus dropout tinggi.
 3. Menggunakan model machine learning atau penerapan EWS (Early Warning System) untuk mengidentifikasi secara dini mahasiswa akan melakukan dropout berdasarkan performa selama berkuliah.
