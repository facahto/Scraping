import streamlit as st

st.markdown('')
st.markdown('')
st.markdown('Selamat siang Bapak/Ibu,')
st.markdown('perkenalkan saya DINI dari Astra Credit Companies pusat.')
st.markdown('')
st.markdown('Selamar Bapak/Ibu menjadi pelanggan prioritas ACC, maka dari itu kami menawarkan program tambah mobil untuk bapak/ibu dengan benefit:')
st.write('<div style="margin-left: 40px;">Discount admin 1,5jt rupiah</div>', unsafe_allow_html=True)
st.write('<div style="margin-left: 40px;">Discount asuransi max 2jt rupiah</div>', unsafe_allow_html=True)
st.write('<div style="margin-left: 40px;">Astrapay 1jt rupiah</div>', unsafe_allow_html=True)
st.markdown('')
st.markdown('Dengan rate 3,9%-6,0% DP 20% untuk brand Toyota & Daihatsu')
st.markdown('')
st.markdown('Apakah saya boleh mengetahui unit mana yang bapak/ibu minati agat simulasi perhitungan dapat dikirimkan? ')


col1, col2, col3,col4 = st.columns(4)

next  = col1.button('SAYA BERMINAT')
done  = col2.button('TIDAK BERMINAT')
list_ = []
dict_ = {'domisili':0,'tenor':0,'DP':0,'bayar':0}

if 'Menunggu' not in st.session_state:
    st.session_state['Menunggu'] = False

if next:
    st.write('---')
    with st.form("my_form"):
        st.write("Baik, saya coba perhitungkan simulasi kreditnya, ya pak/bu. Untuk mengetahui harga mobil, boleh diinformasikan KTP dari daerah mana Bapak/Ibu?")
        dom = st.text_input('Asal KTP')
        st.write("Baik, untuk tenor rencana mau yang berapa tahun, pak/bu?")
        tenor = st.text_input('Tenor')
        st.write("Baik, untuk DP rencana mau yang berapa persen, pak/ibu? atau mau coba DP minimal kami sebesar 20%?")
        DP = st.text_input('Persenan DP')
        st.write('Baik, untuk pembayaran pertamanya mau ADDM atau ADDB?')
        bayar = st.text_input('pembayaran pertama (ADDM/ADDB)')
        dict_['dom'] = dom
        dict_['tenor'] = tenor
        dict_['DP'] = DP
        dict_['bayar'] = bayar
        st.write('Apakah bapak/ibu bersedia menunggu?')
        l1, l2 = st.columns(2)
        agree = l1.checkbox('Menunggu')
        donta = l1.checkbox('via Whatsapp')
        if agree:
            st.session_state['Menunggu'] = not st.session_state['MENUNGGU']
            st.write('Baik Bapak/Ibu, saya simulasikan perhitungan kreditnya terlebih dahulu. Mohon ditunggu sebentar.')
        if donta:
            st.write('Baik Bapak/Ibu, saya simulasikan perhitungan kreditnya terlebih dahulu. Mohon ditunggu, saya akan segera kirimkan simulasi perhitungan kredit melalui nomor Whatsapp Bapak/Ibu yang saat ini saya hubungi. Terima kasih dan sehat selalu pak/bu')
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

if done:
    st.write('kdkd')




