import streamlit as st

# Judul Aplikasi
st.set_page_config(page_title="Aplikasi Multi Fitur", layout="centered")
st.title("Aplikasi Multi Fitur dengan Streamlit")


# Membuat menu navigasi
menu = st.sidebar.radio("Pilih Fitur", ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"])

# ==============================
# 1. KALKULATOR SEDERHANA
# ==============================
if menu == "Kalkulator":
    st.header("📌 Kalkulator Sederhana")
    st.write("Masukkan dua angka lalu pilih operator untuk melihat hasilnya.")

    # Input angka
    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)

    # Pilih operator
    operator = st.selectbox("Pilih operator", ["+", "-", "×", "÷"])

    # Hitung hasil
    if operator == "+":
        hasil = a + b
    elif operator == "-":
        hasil = a - b
    elif operator == "×":
        hasil = a * b
    elif operator == "÷":
        if b != 0:
            hasil = a / b
        else:
            hasil = "Error: Pembagian dengan nol!"

    st.success(f"Hasil: {a} {operator} {b} = {hasil}")


# ==============================
# 2. KONVERSI SUHU
# ==============================
elif menu == "Konversi Suhu":
    st.header("🌡️ Konversi Suhu")
    st.write("Masukkan nilai suhu dalam salah satu satuan, lalu pilih konversi yang diinginkan.")

    # Input nilai suhu
    nilai = st.number_input("Masukkan nilai suhu", value=0.0)
    asal = st.selectbox("Dari", ["Celcius", "Reamur", "Fahrenheit"])
    tujuan = st.selectbox("Ke", ["Celcius", "Reamur", "Fahrenheit"])

    hasil = None
    # Konversi suhu
    if asal == "Celcius":
        if tujuan == "Celcius":
            hasil = nilai
        elif tujuan == "Reamur":
            hasil = (4/5) * nilai
        elif tujuan == "Fahrenheit":
            hasil = (9/5) * nilai + 32

    elif asal == "Reamur":
        if tujuan == "Celcius":
            hasil = (5/4) * nilai
        elif tujuan == "Reamur":
            hasil = nilai
        elif tujuan == "Fahrenheit":
            hasil = (9/4) * nilai + 32

    elif asal == "Fahrenheit":
        if tujuan == "Celcius":
            hasil = (5/9) * (nilai - 32)
        elif tujuan == "Reamur":
            hasil = (4/9) * (nilai - 32)
        elif tujuan == "Fahrenheit":
            hasil = nilai

    st.success(f"Hasil konversi: {nilai} {asal} = {hasil} {tujuan}")


# ==============================
# 3. DERET FIBONACCI
# ==============================
elif menu == "Deret Fibonacci":
    st.header("🔢 Deret Fibonacci")
    st.write("Masukkan jumlah n untuk menampilkan deret Fibonacci.")

    n = st.number_input("Masukkan jumlah n", min_value=1, step=1)

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[:n]

    if st.button("Tampilkan Deret Fibonacci"):
        deret = fibonacci(n)
        st.success(f"Deret Fibonacci {n} bilangan pertama: {deret}")
