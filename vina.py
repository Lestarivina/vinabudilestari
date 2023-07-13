import streamlit as st 
from PIL import Image 


st.header("Vina Budi Lestari :wave:")
st.write("""
		Universitas Nasional Karangturi
		"""
		)
image = Image.open("Vina.jpeg")
st.image(image, width=200)


st.info("""Saya adalah mahasiswa prodi manajemen informasi kesehatan fakultas kesehatan di Universitas Nasional Karangturi,
		Di Universitas Nasional Karangturi saya juga aktif dalam Organisasi HIMA atau Himpunan Mahasiswa
		"""
		)

st.markdown(" ## Biodata", unsafe_allow_html=True)
st.write("Nama :")
nama = ["Vina Budi Lestari"]
pilih_nama = st.selectbox("", nama)
if pilih_nama == "Vina Budi Lestari":
	st.write("")

st.write("Prodi :")
prodi = ["MIK"]
pilih_prodi = st.selectbox("", prodi)
if pilih_prodi == "MIK":
	st.write("")

st.write("Fakultas :")
fakultas = ["Kesehatan"]
pilih_fakultas = st.selectbox("", fakultas)
if pilih_fakultas == "kesehatan":
	st.write("")

st.write("Alamat :")
alamat = ["Wonosobo"]
pilih_alamat = st.selectbox("", alamat)
if pilih_alamat == "wonosobo":
	st.write("")

st.markdown(" ## Education", unsafe_allow_html=True)
st.info("""2010-2016 SD N 1 PERBOTO
		"""
		)
st.info(""":point: 2016-2019 SMP N 2 KALIKAJAR
		"""
		)
st.info("""2019-2022 MAN 2 WONOSOBO
		"""
		)

st.markdown(" ## Skill", unsafe_allow_html=True)
st.info("""Dapat menganalisis data 
		"""
		)
st.info("""Bisa menggunakan ICD 10 dengan baik 
		"""
		)
st.info("""Bisa mengoperasikan microsoft office
		"""
		)



st.markdown(" ## MIK", unsafe_allow_html=True)
st.info("""Manajemen informasi kesehatan mencakup seluruh aktifitas pengelolaan rekam medis yang dimulai dari pengelolaan dan 
		penataan berkas sampai kepada pengelolaan data hingga menghasilkan sebuah informasi kesehatan sesuai kebutuhan.Sedangkan fungsi manajemen pelayanan kesehatan tidak melepaskan fungsi-fungsi manajemen secara umum yang meliputi perencanaan, pengorganisasian, penempatan dan pembinaan staf yang sesuai, sistem penganggaran, sistem pelaksanaan, pengendalian, monitoring dan evaluasi.
		"""
		)
 

st.markdown(" :mailbox: Kotak Saran")
if "my_input" not in st.session_state:
	st.session_state["my_input"]= ""

my_input = st.text_input("Masukan saran di sini", st.session_state["my_input"])
submit = st.button("submit")
if submit:
	st.session_state["my_input"] = my_input
	st.write("Anda telah memasukkan data text:", my_input)


st.markdown(" ## Social Media", unsafe_allow_html=True)
image = Image.open("Instagram.png")
st.image(image, width=40)
st.write("[Instagram >](https://www.instagram.com/vinalstr_24/saved/)")
image = Image.open("wa.jpg")
st.image(image, width=40)
st.write("[whatsapp >](https://https://web.whatsapp.com//vinalstr_24/saved/)")
image = Image.open("TikTok.png")
st.image(image, width=40)
st.write("[Tiktok >](https://https://https://www.tiktok.com/foryou?lang=en//vinalstr_24/saved/)")
image = Image.open("fb.png")
st.image(image, width=40)
st.write("[Facebook >](https://www.facebook.com/home.php//vinalstr_24/saved/)")







	
