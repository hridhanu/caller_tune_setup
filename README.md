# **📞 Caller Tune Setup - Modern GUI Application 🎵**

A real-life usable Caller Tune Setup application with a sleek, modern GUI built using CustomTkinter & Pygame. This project allows users to set up caller tunes for their mobile numbers with an intuitive, stylish, and interactive interface.

---

## **✨ Features**

✅ **Modern UI with CustomTkinter** - Dark theme, sleek buttons, and a professional look\
✅ **Phone Number Verification** - Ensures a valid 10-digit number before proceeding\
✅ **Dynamic Language & Category Selection** - Supports **English, Hindi, and Bengali** with multiple categories\
✅ **Scrollable & Clickable Song Selection** - Songs appear as **interactive buttons** inside a smooth scrollable frame\
✅ **Music Playback with Pygame** - Play and stop any song before setting it as a caller tune\
✅ **Realistic Caller Tune Setup** - Mimics real-world functionality for easy user experience\
✅ **Error Handling & User Feedback** - Proper validation, file existence checks, and clear messages

---

## **📂 Folder Structure**

```
CallerTuneSetup/
│── English/
│   ├── Love/
│   │   ├── song1.mp3
│   │   ├── song2.mp3
│   ├── Chill/
│   ├── Patriotic/
│   ├── Emotional/
│── Hindi/
│── Bengali/
│── proj1.py  # Main Python File
│── requirements.txt  # Dependencies
│── README.md  # Project Documentation
```

*(Make sure to add MP3 files inside the respective folders to test the application.)*

---

## **🚀 How to Run the Project?**

### **1️⃣ Install Dependencies**

Make sure you have Python installed. Then, install required libraries:

```bash
pip install customtkinter pygame
```

### **2️⃣ Run the Application**

```bash
python proj1.py
```

---

## **🎮 Usage Guide**

### **🔹 Step 1: Enter Your Phone Number**

- Enter a **10-digit valid phone number** and click **Verify** ✅
- If valid, language selection becomes active.

### **🔹 Step 2: Select Language & Category**

- Choose **Language** → English, Hindi, or Bengali 🌍
- Choose **Category** → Love, Chill, Patriotic, Emotional 🎶

### **🔹 Step 3: Load & Play Songs**

- Click **Load Songs** → Displays available songs as **buttons** 📜
- Click a **Song Button** → Song starts playing immediately 🔊

### **🔹 Step 4: Set Caller Tune**

- Click **"Set as Caller Tune"** → Confirms selection and stops playback 📞

---

## **🛠 Tech Stack**

- **Python** - Core programming language
- **CustomTkinter** - Advanced GUI framework for modern UI
- **Pygame Mixer** - Music playback functionality

---

## **🔧 Future Improvements**

- ✅ **Save Caller Tune Preferences** for automatic setup next time
- ✅ **More Language Support** - Add regional Indian languages
- ✅ **Online Song Fetching** - Stream songs from the internet instead of local storage

## NOTE: not including music due to size add music as per your need in every folder
