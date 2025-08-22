---
title: Apa itu HTTP(S)?
date: 2025-03-25 13:50:00 +07:00
tags: ["HTTP", "HTTPS", "WebSecurity"]
comments: true
---

## Apa itu HTTP?

HTTP (HyperText Transfer Protocol) adalah protokol yang digunakan untuk mentransmisikan data di web. Setiap kali kamu mengakses situs web, perangkatmu menggunakan HTTP untuk berkomunikasi dengan server dan mengambil halaman web yang diminta. HTTP pertama kali dikembangkan oleh Tim Berners-Lee dan timnya antara tahun 1989-1991.

HTTP memungkinkan pengiriman berbagai jenis data seperti:

- **HTML** (struktur halaman web)
- **Gambar** (JPEG, PNG, GIF)
- **Video** (MP4, WebM)
- **File lain** (PDF, dokumen, dll.)

Namun, HTTP memiliki kelemahan utama: **data yang dikirim tidak dienkripsi**. Artinya, jika seseorang menyadap koneksi antara browser dan server, mereka bisa melihat semua data yang dikirim, termasuk informasi sensitif seperti kredensial login.

## Apa itu HTTPS?

HTTPS (HyperText Transfer Protocol Secure) adalah versi aman dari HTTP. Bedanya, **HTTPS menggunakan enkripsi melalui protokol TLS (dulu dikenal sebagai SSL)**. Ini berarti data yang dikirim antara browser dan server menjadi **terenkripsi**, sehingga tidak bisa dengan mudah dibaca oleh pihak ketiga.

Keuntungan HTTPS:

1. **Keamanan Data** – Informasi yang dikirim dan diterima tidak bisa disadap atau dimanipulasi.
2. **Keaslian Website** – HTTPS memastikan kamu terhubung ke server yang benar, bukan situs palsu yang dibuat untuk mencuri data.
3. **Kepercayaan Pengguna** – Browser modern menandai situs yang tidak menggunakan HTTPS sebagai "Tidak Aman", sehingga pengguna lebih percaya pada situs yang memiliki HTTPS.
4. **SEO Lebih Baik** – Google memberikan peringkat lebih tinggi pada situs yang menggunakan HTTPS.

## Analogi Sederhana

Bayangkan HTTP seperti **mengirim kartu pos**. Semua orang yang menangani kartu pos itu (seperti tukang pos atau orang lain yang menemukannya) bisa membaca isi pesan.

Sebaliknya, HTTPS seperti **mengirim surat dalam amplop yang terkunci**. Hanya penerima yang memiliki kunci yang bisa membaca isinya, sehingga lebih aman dari orang lain yang mencoba mengintip.

Dengan kata lain, jika kamu mengunjungi situs yang membutuhkan informasi sensitif (seperti login atau transaksi), pastikan alamatnya diawali dengan `https://` untuk memastikan keamanan datamu.
