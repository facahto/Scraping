import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ['Branchless','Summary','Bucket Leads'],
    )


if selected == 'Branchless':
    left_co, cent_co,last_co,c4= st.columns(4)
    with cent_co:
        st.image(image, width = 350)
    with left_co:
        st.write(' ')
    with last_co:
        st.write(' ')
if selected == 'Summary':
    st.title('Summary')
    col1,col2 = st.columns([3,1])
    summary_data = col1.dataframe(summary[:-1],hide_index=True)
    total_summary = summary.tail(1).rename(columns={'TELEMARKETING': ' '*35})
    total_summary = col1.dataframe(total_summary,hide_index=True)

    col2.markdown('')
    col2.markdown('')
    col2.markdown('')
    
if selected == 'Bucket Leads':

    st.write("Baik, saya coba perhitungkan simulasi kreditnya, ya pak/bu. Untuk mengetahui harga mobil, boleh diinformasikan KTP dari daerah mana Bapak/Ibu?")
    dom = st.text_input('Asal KTP')
    st.write("Baik, untuk tenor rencana mau yang berapa tahun, pak/bu?")
    tenor = st.text_input('Tenor')
    st.write("Baik, untuk DP rencana mau yang berapa persen, pak/ibu? atau mau coba DP minimal kami sebesar 20%?")
    DP = st.text_input('Persenan DP')
    st.write('Baik, untuk pembayaran pertamanya mau ADDM atau ADDB?')
    bayar = st.text_input('pembayaran pertama (ADDM/ADDB)')

    st.write('Apakah bapak/ibu bersedia menunggu?')
    l1, l2 = st.columns(2)
    agree = l1.checkbox('Menunggu')
    donta = l1.checkbox('via Whatsapp')
    if agree:
        st.session_state['Menunggu'] = not st.session_state['MENUNGGU']
        st.write('Baik Bapak/Ibu, saya simulasikan perhitungan kreditnya terlebih dahulu. Mohon ditunggu sebentar.')
    if donta:
        st.write('Baik Bapak/Ibu, saya simulasikan perhitungan kreditnya terlebih dahulu. Mohon ditunggu, saya akan segera kirimkan simulasi perhitungan kredit melalui nomor Whatsapp Bapak/Ibu yang saat ini saya hubungi. Terima kasih dan sehat selalu pak/bu')




