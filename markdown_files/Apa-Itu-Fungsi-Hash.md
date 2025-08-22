---
title: Apa Itu Fungsi Hash?
date: 2025-04-09 03:45:00 +07:00
tags: ["HashFunction", "Cryptography", "HashCollision", "MD5", "SHA1", "Integrity", "Hashing"]
comments: true
---

## Definisi Fungsi Hash

Fungsi hash **berbeda dengan enkripsi**. Fungsi hash:

- **Tidak menggunakan kunci**
- Tidak dirancang untuk dibalik (irreversible)
- Menghasilkan output dengan **ukuran tetap**
- Bisa menerima input dengan **ukuran arbitrer (bebas)**
- Output sulit diprediksi dan akan **berubah drastis** hanya dengan perubahan kecil pada input (efek avalanche)

Contoh:
- Huruf `T` = `01010100` (hex: 54)
- Huruf `U` = `01010101` (hex: 55)
  → Hanya beda **1 bit**, tapi hasil hash sangat berbeda.

### Ilustrasi Perbedaan Hash:

```bash
strategos@g5000 ~> cat file1.txt
T⏎
strategos@g5000 ~> cat file2.txt
U⏎
strategos@g5000 ~> hexdump -C file1.txt
00000000  54                                                |T|
00000001
strategos@g5000 ~> hexdump -C file2.txt
00000000  55                                                |U|
00000001
strategos@g5000 ~> md5sum *.txt
b9ece18c950afbfa6b0fdbfa4ff731d3  file1.txt
4c614360da93c0a041b22e537de151eb  file2.txt
strategos@g5000 ~> sha1sum *.txt
c2c53d66948214258a26ca9ca845d7ac0c17f8e7  file1.txt
b2c7c0caa10a0cca5ea7d69e54018ae0c0389dd6  file2.txt
strategos@g5000 ~> sha256sum *.txt
e632b7095b0bf32c260fa4c539e9fd7b852d0de454e9be26f24d0d6f91d069d3  file1.txt
a25513c7e0f6eaa80a3337ee18081b9e2ed09e00af8531c8f7bb2542764027e7  file2.txt
```

| File | Isi | MD5 | SHA1 | SHA-256 |
|------|-----|-----|------|----------|
| file1.txt | `T` | `b9ece18c950afbfa6b0fdbfa4ff731d3` | `c2c53d66948214258a26ca9ca845d7ac0c17f8e7` | `e632b7095b0bf32c260fa4c539e9fd7b852d0de454e9be26f24d0d6f91d069d3` |
| file2.txt | `U` | `4c614360da93c0a041b22e537de151eb` | `b2c7c0caa10a0cca5ea7d69e54018ae0c0389dd6` | `a25513c7e0f6eaa80a3337ee18081b9e2ed09e00af8531c8f7bb2542764027e7` |

> Format umum output hash:
> - **Hexadecimal**: digunakan oleh `md5sum`, `sha1sum`, `sha256sum`, dll.
> - Setiap byte direpresentasikan sebagai **2 digit hex**

## Mengapa Hashing Penting?

Hashing digunakan luas di berbagai sistem keamanan, terutama:

- **Verifikasi integritas data** (file tidak berubah selama proses transfer atau penyimpanan)
- **Penyimpanan password** dengan aman (tanpa menyimpan teks asli password)
- **Otentikasi sistem** seperti login di website atau komputer

Contoh nyata:
- Saat login ke TryHackMe atau sistem lain, password kamu tidak disimpan langsung.
- Yang disimpan adalah **hash** dari password.
- Saat kamu login, sistem akan menghitung hash dari password yang kamu masukkan dan membandingkannya dengan hash yang disimpan.

## Rumus Hashing

> 2 ^ nilai bit hash = jumlah input yang bisa diinputkan

Contoh:
- MD5 = 128 bit, `2 ^ 128`
- SHA1 = 160 bit, `2 ^ 160`
- SHA256 = 256 bit, `2 ^ 256`

Misal kamu memiliki output hash 8 bit, maka kemungkinan nilai hashnya `2 ^ 8 = 256 bit`

## Apa Itu *Hash Collision*?

Hash collision terjadi saat **dua input berbeda menghasilkan hash yang sama**. Ini tidak diinginkan dan membahayakan keamanan sistem.

### Kenapa Bisa Terjadi?
Karena:
- Jumlah input = tidak terbatas
- Jumlah output = terbatas (tergantung jumlah bit)
- → *Efek pigeonhole* (lubang merpati): jika ada lebih banyak merpati daripada lubangnya, akan ada tabrakan

### Contoh:
Jika fungsi hash hanya punya 4 bit output, maka hanya ada 16 nilai hash yang mungkin. Jika kita coba lebih dari 16 input, akan ada yang tabrakan.

### Status Keamanan:
- **MD5 dan SHA1** sudah dianggap tidak aman karena **tabrakan bisa direkayasa**
- Contoh:
  - MD5 Collision Demo: menunjukkan dua file berbeda dengan hash MD5 yang sama
  - SHA1: diserang dalam proyek **SHAttered**

> Rekomendasi: Hindari menggunakan MD5 dan SHA1 untuk keperluan keamanan (seperti password hashing atau integritas file penting)
