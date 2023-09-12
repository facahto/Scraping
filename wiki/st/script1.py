import streamlit as st

 
st.write('')
st.write('')
st.write("Baik, saya coba perhitungkan simulasi kreditnya, ya pak/bu. Untuk mengetahui harga mobil, boleh diinformasikan KTP dari daerah mana Bapak/Ibu?")
dom = st.text_input('Asal KTP')
st.write('---')
st.write("Baik, untuk tenor rencana mau yang berapa tahun, pak/bu?")
tenor = st.text_input('Tenor')
st.write('---')
st.write("Baik, untuk DP rencana mau yang berapa persen, pak/ibu? atau mau coba DP minimal kami sebesar 20%?")
DP = st.text_input('Persenan DP')
st.write('---')
st.write('Baik, untuk pembayaran pertamanya mau ADDM atau ADDB?')
bayar = st.text_input('pembayaran pertama (ADDM/ADDB)')
st.write('---')
st.write('Apakah bapak/ibu bersedia menunggu?')
l1, l2,l3,l4 = st.columns(4)
agree = l1.button('Menunggu')
donta = l2.button('via Whatsapp')
if agree:
    st.write('Baik Bapak/Ibu, saya simulasikan perhitungan kreditnya terlebih dahulu. Mohon ditunggu sebentar.')
if donta:
    st.write('Baik Bapak/Ibu, saya simulasikan perhitungan kreditnya terlebih dahulu. Mohon ditunggu, saya akan segera kirimkan simulasi perhitungan kredit melalui nomor Whatsapp Bapak/Ibu yang saat ini saya hubungi. Terima kasih dan sehat selalu pak/bu')

st.write(f'''
        <a target="_self" href="https://acc-astra-kredit.streamlit.app">
            <button>
                Kembali Ke Halaman Utama
            </button>
        </a>
        ''',
        unsafe_allow_html=True)  
