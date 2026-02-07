"""
Synthetic Legal Document Generator for OMBUDSMAN RI Workshop
==============================================================

Generate realistic Indonesian legal documents dengan:
- Proper legal structure (Peraturan, SOP, FAQ)
- Quality variations (HIGH, MEDIUM, LOW)
- Simulated OCR errors
- Ready untuk embedding dalam Kaggle notebooks

Author: Workshop Material Developer
Date: 2025
"""

import random
import re
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
import json


@dataclass
class Document:
    """
    Document data structure
    """
    doc_id: str
    title: str
    category: str
    quality: str
    content: str
    metadata: Dict
    
    def word_count(self) -> int:
        return len(self.content.split())
    
    def char_count(self) -> int:
        return len(self.content)


class OCRErrorSimulator:
    """
    Simulate realistic OCR errors untuk Indonesian legal documents
    """
    
    def __init__(self):
        # Common OCR substitutions
        self.medium_errors = {
            'Indonesia': 'Indqnesia',
            'indonesia': 'indqnesia',
            '0': 'O',
            'Pasal': 'Pasa1',
            'dalam': 'da1am',
            'adalah': 'ada1ah',
            'oleh': 'o1eh',
            'publik': 'pub1ik',
            'lembaga': '1embaga',
            'maladministrasi': 'ma1administrasi',
            'pelayanan': 'pe1ayanan',
            'penyelenggara': 'penye1enggara',
            'kewenangan': 'kewenangan',
            'selanjutnya': 'se1anjutnya',
            'keluhan': 'ke1uhan',
            'perilaku': 'peri1aku',
            'melawan': 'me1awan',
            'melampaui': 'me1ampaui',
            'kelalaian': 'ke1a1aian',
            'kualitas': 'kua1itas',
            'penyelesaian': 'penye1esaian',
            'akuntabilitas': 'akuntabi1itas',
            '2024': '2O24',
            '2023': '2O23',
            '15': 'I5',
            '14': 'I4',
            '60': '6O',
        }
        
        self.severe_errors = {
            'Indonesia': 'lndon3sia',
            'Ombudsman': 'Qmbudsman',
            'Republik': 'Repub1ik',
            'Pasal': 'Pasa1',
            'bahwa': 'bahvva',
            'dengan': 'der1gan',
            'yang': 'yar1g',
            'untuk': 'untuk',
            'dari': 'clari',
            'ini': 'ir1i',
            'atau': 'atav',
            'pada': 'pacla',
            'akan': 'akar1',
            'harus': 'harvs',
            'dapat': 'dapaf',
            'setiap': 'sefiap',
            'antara': 'ar1tara',
            'kepada': 'kepacla',
            'tentang': 'ter1tang',
            'sebagai': 'sebaqai',
        }
    
    def apply_medium_errors(self, text: str, error_rate: float = 0.15) -> str:
        """
        Apply medium level OCR errors
        
        Args:
            text: Original text
            error_rate: Percentage of substitutions to apply
        
        Returns:
            Text dengan simulated OCR errors
        """
        corrupted = text
        
        # Apply errors randomly based on error_rate
        for original, corrupted_version in self.medium_errors.items():
            if random.random() < error_rate:
                corrupted = corrupted.replace(original, corrupted_version)
        
        return corrupted
    
    def apply_severe_errors(self, text: str, error_rate: float = 0.35) -> str:
        """
        Apply severe OCR errors plus spacing issues
        """
        corrupted = text
        
        # Apply severe substitutions
        for original, corrupted_version in self.severe_errors.items():
            if random.random() < error_rate:
                corrupted = corrupted.replace(original, corrupted_version)
        
        # Add spacing issues
        corrupted = self._add_spacing_errors(corrupted)
        
        return corrupted
    
    def _add_spacing_errors(self, text: str) -> str:
        """
        Add excessive or missing spaces
        """
        # Add random extra spaces (5% of spaces become double)
        words = text.split(' ')
        result = []
        for word in words:
            result.append(word)
            if random.random() < 0.05:
                result.append(' ')  # Extra space
        
        return ' '.join(result)


class SyntheticDocumentGenerator:
    """
    Generate realistic Indonesian legal documents
    """
    
    def __init__(self):
        self.ocr_simulator = OCRErrorSimulator()
        self.documents = []
    
    def generate_peraturan(self, doc_num: int, quality: str) -> Document:
        """
        Generate Peraturan Ombudsman document
        """
        topics = [
            ("Standar Pelayanan Pengaduan Masyarakat", "pelayanan pengaduan", "meningkatkan kualitas pelayanan pengaduan"),
            ("Tata Cara Investigasi Laporan Maladministrasi", "investigasi", "menjamin proses investigasi yang objektif dan akuntabel"),
            ("Pengelolaan Rekomendasi dan Tindak Lanjut", "rekomendasi", "memastikan efektivitas pelaksanaan rekomendasi"),
            ("Transparansi Informasi Publik Ombudsman", "transparansi", "meningkatkan keterbukaan informasi kepada publik"),
            ("Kode Etik dan Perilaku Penyelenggara", "etika", "menetapkan standar etika penyelenggara pelayanan publik"),
        ]
        
        topic_data = topics[doc_num % len(topics)]
        title, keyword, tujuan = topic_data
        
        nomor = 10 + doc_num
        
        content = f"""PERATURAN OMBUDSMAN REPUBLIK INDONESIA
NOMOR {nomor} TAHUN 2024
TENTANG {title.upper()}

DENGAN RAHMAT TUHAN YANG MAHA ESA
KETUA OMBUDSMAN REPUBLIK INDONESIA,

Menimbang:
a. bahwa untuk {tujuan} diperlukan pengaturan yang jelas dan komprehensif;
b. bahwa dalam rangka mewujudkan pelayanan publik yang berkualitas, perlu adanya standar dan pedoman yang dapat dijadikan acuan oleh seluruh penyelenggara pelayanan publik;
c. bahwa berdasarkan pertimbangan sebagaimana dimaksud dalam huruf a dan huruf b, perlu menetapkan Peraturan Ombudsman tentang {title};

Mengingat:
1. Undang-Undang Nomor 37 Tahun 2008 tentang Ombudsman Republik Indonesia (Lembaran Negara Republik Indonesia Tahun 2008 Nomor 139, Tambahan Lembaran Negara Republik Indonesia Nomor 4899);
2. Undang-Undang Nomor 25 Tahun 2009 tentang Pelayanan Publik (Lembaran Negara Republik Indonesia Tahun 2009 Nomor 112, Tambahan Lembaran Negara Republik Indonesia Nomor 5038);
3. Peraturan Presiden Nomor 76 Tahun 2013 tentang Pengelolaan Pengaduan Pelayanan Publik;
4. Peraturan Ombudsman Republik Indonesia Nomor 26 Tahun 2017 tentang Tata Cara Penerimaan, Pemeriksaan, dan Penyelesaian Laporan;

MEMUTUSKAN:

Menetapkan: PERATURAN OMBUDSMAN TENTANG {title.upper()}

BAB I
KETENTUAN UMUM

Pasal 1
Dalam Peraturan ini yang dimaksud dengan:
1. Ombudsman Republik Indonesia yang selanjutnya disebut Ombudsman adalah lembaga negara yang mempunyai kewenangan mengawasi penyelenggaraan pelayanan publik baik yang diselenggarakan oleh penyelenggara negara dan pemerintahan termasuk yang diselenggarakan oleh Badan Usaha Milik Negara, Badan Usaha Milik Daerah, dan Badan Hukum Milik Negara serta badan swasta atau perseorangan yang diberi tugas menyelenggarakan pelayanan publik tertentu.
2. Pelayanan Publik adalah kegiatan atau rangkaian kegiatan dalam rangka pemenuhan kebutuhan pelayanan sesuai dengan peraturan perundang-undangan bagi setiap warga negara dan penduduk atas barang, jasa, dan/atau pelayanan administratif yang disediakan oleh penyelenggara pelayanan publik.
3. Penyelenggara Pelayanan Publik yang selanjutnya disebut Penyelenggara adalah setiap institusi penyelenggara negara, korporasi, lembaga independen yang dibentuk berdasarkan undang-undang untuk kegiatan pelayanan publik, dan badan hukum lain yang dibentuk semata-mata untuk kegiatan pelayanan publik.
4. Masyarakat adalah seluruh pihak, baik warga negara maupun penduduk sebagai orang-perseorangan, kelompok, maupun badan hukum yang berkedudukan sebagai penerima manfaat pelayanan publik.
5. Pengaduan adalah penyampaian keluhan yang disampaikan oleh setiap orang kepada Ombudsman atas dugaan maladministrasi dalam penyelenggaraan pelayanan publik.
6. Pelapor adalah orang perseorangan, kelompok orang, atau badan hukum yang menyampaikan laporan kepada Ombudsman.
7. Terlapor adalah penyelenggara pelayanan publik yang dilaporkan kepada Ombudsman.
8. Maladministrasi adalah perilaku atau perbuatan melawan hukum, melampaui wewenang, menggunakan wewenang untuk tujuan lain dari yang menjadi tujuan wewenang tersebut, termasuk kelalaian atau pengabaian kewajiban hukum dalam penyelenggaraan pelayanan publik yang dilakukan oleh penyelenggara negara dan pemerintahan yang menimbulkan kerugian materiil dan/atau immateriil bagi masyarakat dan orang perseorangan.

Pasal 2
Peraturan ini bertujuan untuk:
a. memberikan pedoman dalam {keyword};
b. meningkatkan kualitas penyelenggaraan pelayanan publik;
c. menjamin kepastian hukum dan perlindungan hak-hak masyarakat;
d. mendorong akuntabilitas dan transparansi dalam pelayanan publik;
e. mewujudkan tata kelola pemerintahan yang baik.

Pasal 3
(1) Ruang lingkup Peraturan ini meliputi:
    a. prinsip dan standar {keyword};
    b. mekanisme dan prosedur pelaksanaan;
    c. hak dan kewajiban para pihak;
    d. monitoring dan evaluasi.
(2) Ketentuan dalam Peraturan ini berlaku bagi seluruh penyelenggara pelayanan publik di Indonesia.

BAB II
PRINSIP DAN STANDAR

Pasal 4
Prinsip {keyword} meliputi:
a. transparansi, yaitu pelaksanaan yang terbuka dan dapat diakses oleh masyarakat;
b. akuntabilitas, yaitu dapat dipertanggungjawabkan sesuai dengan ketentuan peraturan perundang-undangan;
c. profesionalitas, yaitu dilaksanakan dengan kompetensi dan keahlian yang memadai;
d. efisiensi, yaitu menggunakan sumber daya secara optimal untuk mencapai hasil yang maksimal;
e. efektivitas, yaitu mencapai tujuan yang telah ditetapkan;
f. keadilan, yaitu memberikan perlakuan yang sama dan tidak diskriminatif;
g. kepastian hukum, yaitu dilaksanakan sesuai dengan peraturan perundang-undangan.

Pasal 5
(1) Standar {keyword} ditetapkan berdasarkan prinsip sebagaimana dimaksud dalam Pasal 4.
(2) Standar sebagaimana dimaksud pada ayat (1) paling sedikit memuat:
    a. persyaratan teknis;
    b. prosedur pelaksanaan;
    c. jangka waktu penyelesaian;
    d. biaya atau tarif;
    e. produk pelayanan;
    f. sarana, prasarana, dan/atau fasilitas;
    g. kompetensi pelaksana;
    h. pengawasan internal;
    i. penanganan pengaduan;
    j. jumlah pelaksana;
    k. jaminan pelayanan;
    l. jaminan keamanan dan keselamatan pelayanan;
    m. evaluasi kinerja pelaksana.

BAB III
MEKANISME DAN PROSEDUR

Pasal 6
(1) Mekanisme {keyword} dilaksanakan secara sistematis dan terstruktur.
(2) Prosedur pelaksanaan sebagaimana dimaksud pada ayat (1) meliputi:
    a. tahap persiapan;
    b. tahap pelaksanaan;
    c. tahap pelaporan;
    d. tahap evaluasi.

Pasal 7
(1) Tahap persiapan sebagaimana dimaksud dalam Pasal 6 ayat (2) huruf a meliputi:
    a. penyiapan sumber daya manusia;
    b. penyiapan sarana dan prasarana;
    c. penyusunan rencana kerja;
    d. sosialisasi kepada pemangku kepentingan.
(2) Tahap pelaksanaan sebagaimana dimaksud dalam Pasal 6 ayat (2) huruf b dilaksanakan sesuai dengan standar yang telah ditetapkan.
(3) Tahap pelaporan sebagaimana dimaksud dalam Pasal 6 ayat (2) huruf c dilakukan secara berkala kepada pimpinan dan pemangku kepentingan terkait.
(4) Tahap evaluasi sebagaimana dimaksud dalam Pasal 6 ayat (2) huruf d dilakukan untuk mengukur efektivitas dan efisiensi pelaksanaan.

Pasal 8
(1) Setiap penyelenggara wajib melaksanakan {keyword} sesuai dengan ketentuan dalam Peraturan ini.
(2) Pelaksanaan sebagaimana dimaksud pada ayat (1) dilakukan dengan mengacu pada standar operasional prosedur yang telah ditetapkan.
(3) Penyelenggara bertanggung jawab atas kualitas pelaksanaan {keyword}.

BAB IV
HAK DAN KEWAJIBAN

Pasal 9
Masyarakat berhak:
a. mendapatkan pelayanan yang berkualitas sesuai dengan standar yang ditetapkan;
b. mendapatkan informasi yang jelas, akurat, dan mudah diakses;
c. menyampaikan pengaduan apabila terdapat penyimpangan;
d. mendapatkan tanggapan atas pengaduan yang disampaikan;
e. mendapatkan perlindungan hukum.

Pasal 10
Masyarakat berkewajiban:
a. mematuhi prosedur yang telah ditetapkan;
b. memberikan informasi yang benar dan lengkap;
c. menghormati hak-hak penyelenggara;
d. ikut serta menjaga kualitas pelayanan.

Pasal 11
Penyelenggara berhak:
a. mendapatkan penghargaan atas kinerja yang baik;
b. mendapatkan perlindungan dalam melaksanakan tugas;
c. mengajukan keberatan atas laporan yang tidak berdasar.

Pasal 12
Penyelenggara berkewajiban:
a. melaksanakan {keyword} sesuai dengan standar yang ditetapkan;
b. memberikan informasi yang jelas dan akurat kepada masyarakat;
c. menangani pengaduan secara cepat dan tepat;
d. melakukan perbaikan berkelanjutan;
e. melaporkan pelaksanaan kegiatan secara berkala.

BAB V
MONITORING DAN EVALUASI

Pasal 13
(1) Ombudsman melakukan monitoring terhadap pelaksanaan Peraturan ini.
(2) Monitoring sebagaimana dimaksud pada ayat (1) dilakukan secara berkala dan/atau sewaktu-waktu.
(3) Hasil monitoring ditindaklanjuti dengan pemberian rekomendasi kepada penyelenggara.

Pasal 14
(1) Evaluasi terhadap pelaksanaan Peraturan ini dilakukan setiap 6 (enam) bulan.
(2) Evaluasi sebagaimana dimaksud pada ayat (1) bertujuan untuk:
    a. mengukur tingkat pencapaian tujuan;
    b. mengidentifikasi hambatan dan kendala;
    c. merumuskan perbaikan dan pengembangan.
(3) Hasil evaluasi disampaikan kepada pemangku kepentingan terkait.

BAB VI
SANKSI

Pasal 15
(1) Penyelenggara yang tidak melaksanakan ketentuan dalam Peraturan ini dikenakan sanksi administratif.
(2) Sanksi administratif sebagaimana dimaksud pada ayat (1) dapat berupa:
    a. teguran tertulis;
    b. penghentian sementara pelayanan;
    c. pencabutan izin.
(3) Pengenaan sanksi dilakukan sesuai dengan tingkat pelanggaran.

BAB VII
KETENTUAN PENUTUP

Pasal 16
Peraturan ini mulai berlaku pada tanggal diundangkan.

Agar setiap orang mengetahuinya, memerintahkan pengundangan Peraturan Ombudsman ini dengan penempatannya dalam Berita Negara Republik Indonesia.

Ditetapkan di Jakarta
pada tanggal 15 Januari 2024

KETUA OMBUDSMAN REPUBLIK INDONESIA,

ttd

MOKHAMMAD NAJIH
"""
        
        # Apply quality degradation
        if quality == "MEDIUM":
            content = self.ocr_simulator.apply_medium_errors(content, error_rate=0.12)
        elif quality == "LOW":
            content = self.ocr_simulator.apply_severe_errors(content, error_rate=0.30)
        
        doc = Document(
            doc_id=f"PER_{doc_num:03d}",
            title=title,
            category="Peraturan",
            quality=quality,
            content=content,
            metadata={
                "nomor": nomor,
                "tahun": 2024,
                "topik": keyword,
                "jumlah_bab": 7,
                "jumlah_pasal": 16
            }
        )
        
        return doc
    
    def generate_sop(self, doc_num: int, quality: str) -> Document:
        """
        Generate SOP document
        """
        topics = [
            ("Penerimaan Pengaduan Masyarakat", "penerimaan", "menerima dan mendokumentasikan pengaduan"),
            ("Verifikasi dan Klasifikasi Pengaduan", "verifikasi", "memverifikasi kelengkapan dan mengklasifikasikan pengaduan"),
            ("Investigasi Lapangan", "investigasi", "melakukan investigasi atas laporan maladministrasi"),
            ("Penyusunan Laporan Hasil Investigasi", "pelaporan", "menyusun laporan hasil investigasi secara sistematis"),
            ("Monitoring Tindak Lanjut Rekomendasi", "monitoring", "memantau pelaksanaan rekomendasi Ombudsman"),
        ]
        
        topic_data = topics[doc_num % len(topics)]
        title, keyword, tujuan = topic_data
        
        nomor = f"OMB-SOP-{100 + doc_num}"
        
        content = f"""STANDAR OPERASIONAL PROSEDUR
{title.upper()}

Nomor SOP: {nomor}
Tanggal Efektif: 01 Februari 2024
Revisi: 01
Halaman: 1 dari 5

=============================================================================
1. TUJUAN
=============================================================================

Standar Operasional Prosedur ini bertujuan untuk {tujuan} secara efektif, efisien, dan akuntabel sesuai dengan ketentuan peraturan perundang-undangan yang berlaku.

=============================================================================
2. RUANG LINGKUP
=============================================================================

SOP ini mencakup seluruh tahapan proses {keyword} yang dilakukan oleh petugas Ombudsman Republik Indonesia, mulai dari tahap persiapan hingga tahap pelaporan dan evaluasi.

=============================================================================
3. DEFINISI DAN ISTILAH
=============================================================================

Dalam SOP ini yang dimaksud dengan:

3.1 Ombudsman
    Ombudsman Republik Indonesia adalah lembaga negara yang mempunyai kewenangan mengawasi penyelenggaraan pelayanan publik.

3.2 Pengaduan
    Pengaduan adalah penyampaian keluhan yang disampaikan oleh setiap orang kepada Ombudsman atas dugaan maladministrasi dalam penyelenggaraan pelayanan publik.

3.3 Pelapor
    Pelapor adalah orang perseorangan, kelompok orang, atau badan hukum yang menyampaikan laporan kepada Ombudsman.

3.4 Terlapor
    Terlapor adalah penyelenggara pelayanan publik yang dilaporkan kepada Ombudsman.

3.5 Maladministrasi
    Maladministrasi adalah perilaku atau perbuatan melawan hukum, melampaui wewenang, menggunakan wewenang untuk tujuan lain, kelalaian atau pengabaian kewajiban hukum dalam penyelenggaraan pelayanan publik.

3.6 Investigasi
    Investigasi adalah rangkaian kegiatan pemeriksaan dan penelaahan yang dilakukan Ombudsman untuk menemukan fakta dan kebenaran atas laporan yang diterima.

=============================================================================
4. DOKUMEN TERKAIT
=============================================================================

4.1 Undang-Undang Nomor 37 Tahun 2008 tentang Ombudsman Republik Indonesia
4.2 Undang-Undang Nomor 25 Tahun 2009 tentang Pelayanan Publik
4.3 Peraturan Presiden Nomor 76 Tahun 2013 tentang Pengelolaan Pengaduan Pelayanan Publik
4.4 Peraturan Ombudsman Nomor 26 Tahun 2017 tentang Tata Cara Penerimaan, Pemeriksaan, dan Penyelesaian Laporan
4.5 Formulir Penerimaan Pengaduan (Form OMB-01)
4.6 Checklist Verifikasi Dokumen (Form OMB-02)
4.7 Berita Acara Investigasi (Form OMB-03)

=============================================================================
5. PROSEDUR PELAKSANAAN
=============================================================================

5.1 TAHAP PERSIAPAN

    5.1.1 Penyiapan Sumber Daya
          a. Petugas {keyword} memastikan kesiapan personil yang kompeten
          b. Menyiapkan formulir dan dokumen yang diperlukan
          c. Memastikan ketersediaan sarana dan prasarana pendukung
          d. Melakukan briefing kepada tim pelaksana
          
          Waktu: 1 hari kerja
          Penanggung Jawab: Koordinator Unit
    
    5.1.2 Penyiapan Sistem Informasi
          a. Memastikan sistem informasi pengaduan berfungsi dengan baik
          b. Melakukan backup data secara berkala
          c. Memastikan keamanan data dan informasi
          d. Menyiapkan akses untuk petugas yang berwenang
          
          Waktu: Berkelanjutan
          Penanggung Jawab: Administrator Sistem

5.2 TAHAP PELAKSANAAN

    5.2.1 Penerimaan Laporan
          a. Menerima laporan dari masyarakat melalui berbagai saluran:
             - Surat langsung
             - Email ke pengaduan@ombudsman.go.id
             - Aplikasi online SP4N-LAPOR
             - Telepon hotline 138
             - Tatap muka langsung
          
          b. Mencatat informasi dasar laporan:
             - Identitas pelapor
             - Identitas terlapor
             - Uraian maladministrasi
             - Bukti-bukti pendukung
          
          c. Memberikan nomor registrasi kepada pelapor
          d. Memberikan tanda terima pengaduan
          
          Waktu: Maksimal 1 hari kerja sejak laporan diterima
          Penanggung Jawab: Petugas Front Office
    
    5.2.2 Verifikasi Kelengkapan
          a. Memeriksa kelengkapan persyaratan administratif:
             - Identitas pelapor yang jelas dan dapat diverifikasi
             - Identitas terlapor yang spesifik
             - Uraian kronologis peristiwa yang jelas
             - Bukti-bukti yang relevan dan memadai
          
          b. Menilai apakah laporan masuk dalam kewenangan Ombudsman
          c. Mengklasifikasikan jenis maladministrasi yang dilaporkan:
             - Penundaan berlarut
             - Penyalahgunaan wewenang
             - Penyimpangan prosedur
             - Permintaan imbalan uang/jasa
             - Tidak memberikan pelayanan
             - Diskriminasi
             - Kolusi
             - Intimidasi
          
          d. Jika tidak lengkap, mengembalikan kepada pelapor dengan catatan kekurangan
          e. Jika lengkap, meneruskan ke tahap berikutnya
          
          Waktu: Maksimal 7 hari kerja
          Penanggung Jawab: Tim Verifikasi
    
    5.2.3 Penelaahan dan Analisis
          a. Melakukan penelaahan mendalam terhadap:
             - Substansi laporan
             - Dokumen pendukung
             - Peraturan perundang-undangan terkait
             - Standar pelayanan yang berlaku
          
          b. Melakukan analisis untuk menentukan:
             - Relevansi laporan dengan kewenangan Ombudsman
             - Prioritas penanganan
             - Metode investigasi yang akan digunakan
             - Estimasi waktu penyelesaian
          
          c. Menyusun rencana investigasi yang meliputi:
             - Ruang lingkup investigasi
             - Metode dan teknik investigasi
             - Tim investigasi
             - Jadwal pelaksanaan
             - Anggaran yang diperlukan
          
          Waktu: Maksimal 14 hari kerja
          Penanggung Jawab: Tim Penelaah
    
    5.2.4 Pelaksanaan Investigasi
          a. Melakukan pengumpulan data dan informasi melalui:
             - Permintaan keterangan tertulis kepada terlapor
             - Pemanggilan saksi untuk dimintai keterangan
             - Pemeriksaan dokumen dan bukti fisik
             - Kunjungan lapangan untuk verifikasi
             - Klarifikasi dengan pihak-pihak terkait
          
          b. Mendokumentasikan seluruh proses investigasi:
             - Berita acara pemeriksaan
             - Notulensi wawancara
             - Foto dan video dokumentasi
             - Salinan dokumen pendukung
          
          c. Menjaga objektivitas dan independensi dalam investigasi
          d. Memberikan kesempatan yang sama kepada semua pihak untuk memberikan keterangan
          
          Waktu: Maksimal 60 hari kerja (dapat diperpanjang 30 hari kerja dengan pemberitahuan)
          Penanggung Jawab: Tim Investigasi

5.3 TAHAP PELAPORAN

    5.3.1 Penyusunan Laporan
          a. Menyusun laporan hasil investigasi yang memuat:
             - Ringkasan eksekutif
             - Latar belakang kasus
             - Uraian kronologis peristiwa
             - Fakta-fakta yang ditemukan
             - Analisis hukum dan kebijakan
             - Kesimpulan
             - Rekomendasi
          
          b. Melakukan quality control terhadap laporan
          c. Mendapatkan validasi dari supervisor
          d. Finalisasi laporan
          
          Waktu: Maksimal 14 hari kerja setelah investigasi selesai
          Penanggung Jawab: Tim Pelaporan
    
    5.3.2 Penyampaian Laporan
          a. Menyampaikan laporan kepada:
             - Pelapor
             - Terlapor
             - Atasan terlapor
             - Pihak terkait lainnya sesuai kebutuhan
          
          b. Memberikan penjelasan atas rekomendasi yang diberikan
          c. Meminta konfirmasi penerimaan laporan
          d. Mencatat tanggal penyampaian untuk keperluan monitoring
          
          Waktu: Maksimal 7 hari kerja setelah laporan final
          Penanggung Jawab: Sekretariat Unit

5.4 TAHAP MONITORING DAN EVALUASI

    5.4.1 Monitoring Tindak Lanjut
          a. Memantau pelaksanaan rekomendasi oleh terlapor
          b. Meminta laporan berkala tentang progress tindak lanjut
          c. Melakukan verifikasi atas tindak lanjut yang dilaporkan
          d. Memberikan asistensi jika diperlukan
          
          Waktu: 60 hari sejak rekomendasi disampaikan (dapat diperpanjang)
          Penanggung Jawab: Tim Monitoring
    
    5.4.2 Evaluasi Proses
          a. Mengevaluasi efektivitas proses {keyword}
          b. Mengidentifikasi hambatan dan kendala
          c. Merumuskan perbaikan untuk peningkatan kualitas
          d. Mendokumentasikan lesson learned
          
          Waktu: Setiap 6 bulan
          Penanggung Jawab: Koordinator Unit

=============================================================================
6. INDIKATOR KINERJA
=============================================================================

6.1 Waktu Penyelesaian
    - Target: 90% kasus selesai dalam waktu yang ditetapkan
    - Pengukuran: Persentase kasus yang selesai tepat waktu

6.2 Kualitas Laporan
    - Target: 95% laporan tidak ada revisi substansial
    - Pengukuran: Persentase laporan yang langsung diterima tanpa revisi major

6.3 Tingkat Kepuasan
    - Target: Indeks kepuasan pelapor minimal 80
    - Pengukuran: Survey kepuasan pelapor

6.4 Tindak Lanjut Rekomendasi
    - Target: 80% rekomendasi ditindaklanjuti
    - Pengukuran: Persentase rekomendasi yang diimplementasikan

=============================================================================
7. PENANGGUNG JAWAB DAN DISTRIBUSI
=============================================================================

Penanggung Jawab Umum: Kepala Kantor Perwakilan/Asisten Ombudsman

Pihak yang Menerima SOP:
- Seluruh unit kerja terkait di Ombudsman RI
- Kantor perwakilan Ombudsman di daerah
- Stakeholder eksternal yang relevan

=============================================================================
8. LAMPIRAN
=============================================================================

Lampiran 1: Formulir Penerimaan Pengaduan (Form OMB-01)
Lampiran 2: Checklist Verifikasi Dokumen (Form OMB-02)
Lampiran 3: Berita Acara Investigasi (Form OMB-03)
Lampiran 4: Template Laporan Hasil Investigasi
Lampiran 5: Flowchart Proses {title}

=============================================================================

Disetujui oleh:

[Jabatan]                           [Jabatan]
[Nama]                              [Nama]
Tanggal: ___________                Tanggal: ___________

=============================================================================
"""
        
        # Apply quality degradation
        if quality == "MEDIUM":
            content = self.ocr_simulator.apply_medium_errors(content, error_rate=0.10)
        elif quality == "LOW":
            content = self.ocr_simulator.apply_severe_errors(content, error_rate=0.28)
        
        doc = Document(
            doc_id=f"SOP_{doc_num:03d}",
            title=title,
            category="SOP",
            quality=quality,
            content=content,
            metadata={
                "nomor": nomor,
                "tahun": 2024,
                "topik": keyword,
                "jumlah_tahap": 4,
                "estimasi_waktu": "60-90 hari kerja"
            }
        )
        
        return doc
    
    def generate_faq(self, doc_num: int, quality: str) -> Document:
        """
        Generate FAQ/Panduan document
        """
        topics = [
            ("Panduan Mengajukan Pengaduan kepada Ombudsman", "pengaduan", "bagaimana cara mengajukan pengaduan"),
            ("FAQ Proses Investigasi Ombudsman", "investigasi", "memahami tahapan investigasi"),
            ("Panduan Memahami Maladministrasi Pelayanan Publik", "maladministrasi", "mengenali bentuk-bentuk maladministrasi"),
            ("FAQ Hak dan Kewajiban Pelapor", "hak pelapor", "memahami hak dan kewajiban"),
            ("Panduan Mengakses Informasi Publik di Ombudsman", "informasi publik", "cara mengakses informasi"),
        ]
        
        topic_data = topics[doc_num % len(topics)]
        title, keyword, deskripsi = topic_data
        
        content = f"""{"="*80}
{title.upper()}
{"="*80}

Edisi: Februari 2024
Diterbitkan oleh: Ombudsman Republik Indonesia

{"="*80}
PENGANTAR
{"="*80}

Panduan ini disusun untuk membantu masyarakat dalam {deskripsi} kepada Ombudsman Republik Indonesia. Dokumen ini berisi informasi penting yang sering ditanyakan oleh masyarakat dan panduan praktis yang mudah dipahami.

Ombudsman Republik Indonesia adalah lembaga negara yang bertugas mengawasi penyelenggaraan pelayanan publik. Kami berkomitmen untuk membantu masyarakat mendapatkan pelayanan publik yang berkualitas, adil, dan sesuai dengan peraturan perundang-undangan.

{"="*80}
BAGIAN 1: PERTANYAAN UMUM
{"="*80}

Q1: Apa itu Ombudsman Republik Indonesia?

A: Ombudsman Republik Indonesia adalah lembaga negara yang mempunyai kewenangan mengawasi penyelenggaraan pelayanan publik. Ombudsman dibentuk berdasarkan Undang-Undang Nomor 37 Tahun 2008 untuk meningkatkan kualitas pelayanan publik dan melindungi hak-hak masyarakat.


Q2: Apa saja kewenangan Ombudsman?

A: Kewenangan Ombudsman meliputi:
   - Menerima laporan atas dugaan maladministrasi dalam penyelenggaraan pelayanan publik
   - Melakukan investigasi atas prakarsa sendiri terhadap dugaan maladministrasi
   - Melakukan investigasi atas laporan masyarakat
   - Memberikan rekomendasi kepada penyelenggara pelayanan publik
   - Memfasilitasi penyelesaian laporan melalui mediasi dan konsiliasi
   - Melakukan upaya pencegahan maladministrasi


Q3: Siapa yang bisa mengajukan laporan ke Ombudsman?

A: Setiap orang atau badan hukum dapat mengajukan laporan ke Ombudsman, termasuk:
   - Warga negara Indonesia
   - Warga negara asing yang tinggal atau berada di Indonesia
   - Badan hukum yang berkedudukan di Indonesia
   - Kelompok masyarakat atau organisasi


Q4: Apa yang dimaksud dengan maladministrasi?

A: Maladministrasi adalah perilaku atau perbuatan melawan hukum, melampaui wewenang, menggunakan wewenang untuk tujuan lain, kelalaian atau pengabaian kewajiban hukum dalam penyelenggaraan pelayanan publik. Contoh maladministrasi meliputi:
   
   a. Penundaan Berlarut
      Tidak menyelesaikan atau melayani sesuatu sesuai waktu yang ditentukan dalam peraturan atau yang dijanjikan oleh pejabat.
   
   b. Penyalahgunaan Wewenang
      Melakukan tindakan di luar kewenangannya atau menyalahgunakan kewenangan yang dimiliki.
   
   c. Penyimpangan Prosedur
      Tidak mengikuti prosedur yang telah ditetapkan dalam peraturan atau standar pelayanan.
   
   d. Permintaan Imbalan
      Meminta uang, barang, atau jasa kepada penerima layanan yang tidak sesuai dengan ketentuan.
   
   e. Tidak Memberikan Pelayanan
      Menolak memberikan pelayanan yang menjadi kewajibannya tanpa alasan yang sah.


Q5: Pelayanan publik apa saja yang bisa dilaporkan?

A: Semua jenis pelayanan publik yang diselenggarakan oleh:
   - Kementerian dan lembaga pemerintah pusat
   - Pemerintah daerah (provinsi, kabupaten, kota)
   - BUMN dan BUMD
   - Badan hukum yang menyelenggarakan pelayanan publik
   
   Contoh: pelayanan administrasi kependudukan, perizinan, pendidikan, kesehatan, kepolisian, perpajakan, keimigrasian, pertanahan, dan lain-lain.

{"="*80}
BAGIAN 2: CARA MENGAJUKAN PENGADUAN
{"="*80}

Langkah 1: PERSIAPAN DOKUMEN

Siapkan dokumen-dokumen berikut:
a. Fotokopi KTP atau identitas diri yang masih berlaku
b. Surat kuasa (jika diwakilkan)
c. Uraian kronologis kejadian secara lengkap dan jelas
d. Bukti-bukti pendukung:
   - Surat-menyurat dengan instansi terkait
   - Foto atau video (jika ada)
   - Bukti pembayaran
   - Dokumen terkait lainnya


Langkah 2: MENYAMPAIKAN LAPORAN

Anda dapat menyampaikan laporan melalui berbagai cara:

a. ONLINE
   - Website: www.ombudsman.go.id
   - Aplikasi SP4N-LAPOR! (download di Play Store/App Store)
   - Email: pengaduan@ombudsman.go.id
   
   Keuntungan: Cepat, praktis, bisa dilakukan kapan saja

b. SURAT TERTULIS
   - Kirim ke alamat: Jl. HR Rasuna Said Kav. C-19, Jakarta Selatan 12920
   - Format bebas atau gunakan formulir yang tersedia di website
   
   Keuntungan: Ada bukti fisik, lebih formal

c. TELEPON
   - Hotline: 138 (bebas pulsa)
   - WhatsApp: 0811-9862-138
   
   Keuntungan: Cepat mendapat respon, bisa konsultasi langsung

d. DATANG LANGSUNG
   - Kantor pusat Jakarta atau kantor perwakilan di 33 provinsi
   - Jam layanan: Senin-Jumat, 08.00-16.00 WIB
   
   Keuntungan: Bisa konsultasi tatap muka, mendapat pendampingan


Langkah 3: MELENGKAPI INFORMASI

Pastikan laporan Anda memuat informasi berikut:

a. Identitas Pelapor
   - Nama lengkap
   - Alamat lengkap
   - Nomor telepon yang dapat dihubungi
   - Email (jika ada)

b. Identitas Terlapor
   - Nama instansi/lembaga
   - Nama pejabat (jika diketahui)
   - Alamat kantor

c. Uraian Kejadian
   - Kapan: waktu kejadian secara spesifik
   - Dimana: tempat kejadian
   - Apa: jenis pelayanan yang bermasalah
   - Bagaimana: kronologi kejadian secara detail
   - Mengapa: dampak yang Anda alami

d. Bukti Pendukung
   - Lampirkan semua dokumen yang relevan
   - Beri keterangan pada setiap dokumen


Langkah 4: MENDAPATKAN NOMOR REGISTRASI

Setelah laporan diterima, Anda akan mendapatkan:
- Nomor registrasi laporan
- Tanda terima pengaduan
- Informasi tentang proses selanjutnya
- Estimasi waktu penyelesaian


Langkah 5: MEMANTAU PROGRESS

Anda dapat memantau perkembangan laporan melalui:
- Website dengan memasukkan nomor registrasi
- Menghubungi petugas yang menangani kasus Anda
- Email notifikasi (jika Anda mendaftar)

{"="*80}
BAGIAN 3: HAL-HAL PENTING YANG PERLU DIKETAHUI
{"="*80}

PERSYARATAN LAPORAN YANG DAPAT DITERIMA:

1. Laporan harus terkait dengan pelayanan publik
2. Laporan disertai identitas yang jelas (tidak anonim)
3. Laporan bukan merupakan hal yang sedang dalam proses pengadilan
4. Laporan bukan perkara yang telah diputus oleh pengadilan dan memiliki kekuatan hukum tetap
5. Substansi laporan bukan mengenai putusan pengadilan


JANGKA WAKTU PENANGANAN:

- Verifikasi kelengkapan: maksimal 7 hari kerja
- Investigasi: maksimal 60 hari kerja (dapat diperpanjang 30 hari)
- Penyampaian hasil: maksimal 7 hari kerja setelah investigasi selesai
- Monitoring tindak lanjut: 60 hari sejak rekomendasi disampaikan


BIAYA:

Seluruh layanan Ombudsman GRATIS. Tidak ada biaya apapun untuk:
- Pengajuan laporan
- Proses investigasi
- Mediasi atau konsiliasi
- Monitoring dan evaluasi

Waspadai tindakan oknum yang meminta imbalan!


HAK-HAK PELAPOR:

1. Mendapatkan perlindungan fisik dan mental
2. Mendapatkan informasi tentang perkembangan laporan
3. Dirahasiakan identitasnya (jika diminta)
4. Mendapatkan hasil investigasi
5. Mendapatkan jawaban atas laporan yang disampaikan


KEWAJIBAN PELAPOR:

1. Memberikan informasi yang benar dan lengkap
2. Kooperatif dalam proses investigasi
3. Tidak menyalahgunakan hak melapor
4. Menjaga kerahasiaan informasi (jika diminta)

{"="*80}
BAGIAN 4: TIPS DAN SARAN
{"="*80}

TIPS MENYUSUN LAPORAN YANG EFEKTIF:

1. Tulis kronologi secara runtut dan jelas
   - Gunakan bahasa yang mudah dipahami
   - Hindari pengulangan informasi
   - Fokus pada fakta, bukan emosi

2. Lampirkan bukti yang relevan
   - Surat korespondensi dengan instansi
   - Bukti pembayaran atau transaksi
   - Foto atau video pendukung
   - Dokumen resmi terkait

3. Spesifikkan tuntutan Anda
   - Apa yang Anda harapkan dari laporan ini?
   - Apa solusi yang Anda inginkan?

4. Pastikan data kontak Anda benar
   - Periksa ulang nomor telepon
   - Pastikan email aktif
   - Cantumkan alamat yang jelas


APA YANG TIDAK BISA DITANGANI OMBUDSMAN:

1. Perkara yang sedang dalam proses peradilan
2. Perkara yang sudah diputus pengadilan (inkracht)
3. Sengketa perdata antar individu
4. Sengketa bisnis murni
5. Dugaan tindak pidana (harus ke kepolisian)
6. Masalah internal perusahaan swasta (kecuali pelayanan publik)


ALTERNATIF PENYELESAIAN:

Jika kasus Anda tidak bisa ditangani Ombudsman, Anda bisa ke:
- Kepolisian (untuk dugaan pidana)
- Pengadilan (untuk sengketa perdata)
- Komisi Yudisial (untuk perilaku hakim)
- KPPU (untuk persaingan usaha)
- OJK (untuk jasa keuangan)
- Lembaga perlindungan konsumen

{"="*80}
KONTAK DAN INFORMASI
{"="*80}

KANTOR PUSAT:
Ombudsman Republik Indonesia
Jl. HR Rasuna Said Kav. C-19
Jakarta Selatan 12920

KONTAK:
Telepon: (021) 5269 3737
Hotline: 138 (bebas pulsa)
WhatsApp: 0811-9862-138
Email: pengaduan@ombudsman.go.id
Website: www.ombudsman.go.id

MEDIA SOSIAL:
Twitter: @OmbudsmanRI
Facebook: Ombudsman Republik Indonesia
Instagram: @ombudsmanri
YouTube: Ombudsman RI

JAM PELAYANAN:
Senin - Kamis: 08.00 - 16.00 WIB
Jumat: 08.00 - 16.30 WIB
Sabtu, Minggu, Libur Nasional: Tutup

KANTOR PERWAKILAN:
Ombudsman memiliki perwakilan di 33 provinsi seluruh Indonesia.
Untuk informasi alamat dan kontak perwakilan, kunjungi:
www.ombudsman.go.id/perwakilan

{"="*80}
PENUTUP
{"="*80}

Ombudsman hadir untuk membantu Anda mendapatkan pelayanan publik yang berkualitas. Jangan ragu untuk mengajukan laporan jika Anda mengalami maladministrasi dalam pelayanan publik.

Ingat:
- Layanan Ombudsman GRATIS
- Identitas Anda dijaga kerahasiaannya
- Anda dilindungi selama proses investigasi
- Proses transparan dan akuntabel

Mari bersama-sama wujudkan pelayanan publik yang lebih baik!

{"="*80}
Dokumen ini dapat diunduh di: www.ombudsman.go.id/publikasi
Untuk informasi lebih lanjut, hubungi hotline 138
{"="*80}
"""
        
        # Apply quality degradation
        if quality == "MEDIUM":
            content = self.ocr_simulator.apply_medium_errors(content, error_rate=0.08)
        elif quality == "LOW":
            content = self.ocr_simulator.apply_severe_errors(content, error_rate=0.25)
        
        doc = Document(
            doc_id=f"FAQ_{doc_num:03d}",
            title=title,
            category="FAQ/Panduan",
            quality=quality,
            content=content,
            metadata={
                "tahun": 2024,
                "topik": keyword,
                "target_audience": "Masyarakat umum",
                "format": "Q&A dan panduan"
            }
        )
        
        return doc
    
    def generate_all_documents(self) -> List[Document]:
        """
        Generate complete dataset: 15 documents
        - 5 Peraturan (2 HIGH, 2 MEDIUM, 1 LOW)
        - 5 SOP (2 HIGH, 2 MEDIUM, 1 LOW)
        - 5 FAQ (3 HIGH, 2 MEDIUM)
        """
        documents = []
        
        # Peraturan: 5 documents
        qualities_per = ["HIGH", "HIGH", "MEDIUM", "MEDIUM", "LOW"]
        for i, quality in enumerate(qualities_per):
            doc = self.generate_peraturan(i, quality)
            documents.append(doc)
            print(f"Generated: {doc.doc_id} - {doc.title} ({doc.quality})")
        
        # SOP: 5 documents
        qualities_sop = ["HIGH", "HIGH", "MEDIUM", "MEDIUM", "LOW"]
        for i, quality in enumerate(qualities_sop):
            doc = self.generate_sop(i, quality)
            documents.append(doc)
            print(f"Generated: {doc.doc_id} - {doc.title} ({doc.quality})")
        
        # FAQ: 5 documents
        qualities_faq = ["HIGH", "HIGH", "HIGH", "MEDIUM", "MEDIUM"]
        for i, quality in enumerate(qualities_faq):
            doc = self.generate_faq(i, quality)
            documents.append(doc)
            print(f"Generated: {doc.doc_id} - {doc.title} ({doc.quality})")
        
        self.documents = documents
        return documents
    
    def export_as_python_dict(self, output_file: str = "synthetic_documents.py"):
        """
        Export documents as Python dictionary untuk embedding dalam notebook
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('"""\n')
            f.write('Synthetic Documents for OMBUDSMAN RI Workshop\n')
            f.write('Generated dataset dengan 15 realistic legal documents\n')
            f.write('"""\n\n')
            
            f.write('SYNTHETIC_DOCUMENTS = [\n')
            for doc in self.documents:
                doc_dict = asdict(doc)
                f.write('    {\n')
                for key, value in doc_dict.items():
                    if isinstance(value, str):
                        # Escape quotes dan newlines
                        escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                        f.write(f'        "{key}": """{value}""",\n')
                    else:
                        f.write(f'        "{key}": {repr(value)},\n')
                f.write('    },\n')
            f.write(']\n')
        
        print(f"\nExported as Python dict: {output_file}")
    
    def export_as_text_files(self, output_dir: str = "synthetic_docs_txt"):
        """
        Export each document as separate .txt file untuk afternoon session
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        for doc in self.documents:
            filename = f"{doc.doc_id}_{doc.quality}.txt"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"TITLE: {doc.title}\n")
                f.write(f"CATEGORY: {doc.category}\n")
                f.write(f"QUALITY: {doc.quality}\n")
                f.write(f"DOC_ID: {doc.doc_id}\n")
                f.write("="*80 + "\n\n")
                f.write(doc.content)
            
            print(f"Exported: {filepath}")
        
        print(f"\nAll documents exported to: {output_dir}/")
    
    def export_statistics(self, output_file: str = "dataset_statistics.txt"):
        """
        Export dataset statistics
        """
        if not self.documents:
            print("No documents to export statistics for.")
            return
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("SYNTHETIC DATASET STATISTICS\n")
            f.write("="*80 + "\n\n")
            
            # Overall stats
            f.write(f"Total Documents: {len(self.documents)}\n\n")
            
            # By category
            f.write("BY CATEGORY:\n")
            categories = {}
            for doc in self.documents:
                categories[doc.category] = categories.get(doc.category, 0) + 1
            for cat, count in categories.items():
                f.write(f"  {cat}: {count} documents\n")
            f.write("\n")
            
            # By quality
            f.write("BY QUALITY:\n")
            qualities = {}
            for doc in self.documents:
                qualities[doc.quality] = qualities.get(doc.quality, 0) + 1
            for qual, count in qualities.items():
                f.write(f"  {qual}: {count} documents\n")
            f.write("\n")
            
            # Size statistics
            f.write("SIZE STATISTICS:\n")
            word_counts = [doc.word_count() for doc in self.documents]
            char_counts = [doc.char_count() for doc in self.documents]
            
            import statistics
            f.write(f"  Average words per document: {statistics.mean(word_counts):.0f}\n")
            f.write(f"  Min words: {min(word_counts)}\n")
            f.write(f"  Max words: {max(word_counts)}\n")
            f.write(f"  Average characters: {statistics.mean(char_counts):.0f}\n")
            f.write("\n")
            
            # Document list
            f.write("="*80 + "\n")
            f.write("DOCUMENT LIST\n")
            f.write("="*80 + "\n\n")
            
            for doc in self.documents:
                f.write(f"{doc.doc_id} | {doc.category:15} | {doc.quality:6} | {doc.word_count():5} words | {doc.title}\n")
        
        print(f"\nStatistics exported: {output_file}")


# Main execution
if __name__ == "__main__":
    print("="*80)
    print("SYNTHETIC DOCUMENT GENERATOR")
    print("OMBUDSMAN RI Workshop")
    print("="*80 + "\n")
    
    # Initialize generator
    generator = SyntheticDocumentGenerator()
    
    # Generate all documents
    print("Generating synthetic documents...\n")
    documents = generator.generate_all_documents()
    
    print(f"\n{'='*80}")
    print(f"GENERATION COMPLETE: {len(documents)} documents created")
    print(f"{'='*80}\n")
    
    # Export in multiple formats
    print("Exporting documents...\n")
    
    # 1. Python dict for inline embedding
    generator.export_as_python_dict("synthetic_documents.py")
    
    # 2. Text files for afternoon session
    generator.export_as_text_files("synthetic_docs_txt")
    
    # 3. Statistics
    generator.export_statistics("dataset_statistics.txt")
    
    print("\n" + "="*80)
    print("ALL EXPORTS COMPLETE!")
    print("="*80)
    print("\nFiles generated:")
    print("  1. synthetic_documents.py - Python dict untuk Kaggle notebooks")
    print("  2. synthetic_docs_txt/ - Individual .txt files untuk afternoon session")
    print("  3. dataset_statistics.txt - Dataset overview")
    print("\nReady untuk workshop integration!")