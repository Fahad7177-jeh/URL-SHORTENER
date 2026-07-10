# 🔗 URL Shortener

A simple and efficient **URL Shortener** web application built using **Python, Flask, and MySQL**. This application converts long URLs into short, unique links, redirects users to the original website, prevents duplicate entries, and tracks the number of times each shortened URL has been accessed.

---

## 🚀 Features

- 🔗 Convert long URLs into short URLs
- ♻️ Prevent duplicate URL generation
- 🌐 Redirect shortened URLs to the original website
- 📊 Track click count for every shortened URL
- 💾 Store URL mappings in MySQL
- 🎨 Clean and responsive user interface
- 🔒 Generate unique URLs using SHA-256 and Base64

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Flask | Web Framework |
| MySQL | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| SHA-256 | URL Hashing |
| Base64 | Short URL Encoding |
| python-dotenv | Environment Variables |

---

## 📂 Project Structure

```text
URL-Shortener/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── screenshots/
│   ├── home-page.png
│   ├── enter-url.png
│   ├── generated-url.png
│   ├── redirect.png
│   └── database.png
│
├── .env
├── app.py
├── requirements.txt
└── README.md
```

---

## 🗄️ Database

### Database Name

```text
url_shortener
```

### Table Name

```text
url_mapping
```

### Table Structure

| Column | Description |
|---------|-------------|
| id | Unique ID |
| long_url | Original URL |
| short_url | Generated Short URL |
| clicks | Number of Visits |
| created_at | URL Creation Time |

---

## ⚙️ Project Workflow

### Step 1

User enters a long URL.

↓

### Step 2

Flask receives the request.

↓

### Step 3

The application checks whether the URL already exists in the database.

↓

### Step 4

If the URL already exists, the previously generated short URL is returned.

↓

### Step 5

Otherwise, a new short URL is generated using SHA-256 hashing and Base64 encoding.

↓

### Step 6

The generated URL mapping is stored in the MySQL database.

↓

### Step 7

The shortened URL is displayed to the user.

↓

### Step 8

When the shortened URL is opened:

- Click count increases by 1
- User is redirected to the original website

---

# 📸 Project Screenshots

## 🏠 Home Page

The application's landing page where users can paste their long URL.

<img width="684" height="363" alt="image" src="https://github.com/user-attachments/assets/44dfcc2b-4f05-423c-8511-c4daf199a20e" />


---

## ✍️ Enter Long URL

Users enter a valid long URL before generating a shortened link.

<img width="697" height="386" alt="image" src="https://github.com/user-attachments/assets/53420bd7-7b7e-492b-8347-3f6577cd7085" />


---

## 🔗 Short URL Generated

The application generates a unique shortened URL that can be shared and accessed.

<img width="735" height="374" alt="image" src="https://github.com/user-attachments/assets/f34bac83-8ca8-4ff0-a1f1-2a0add11e47c" />


---

## 🌐 Redirect to Original Website

Opening the shortened URL automatically redirects users to the original website.

<img width="698" height="344" alt="image" src="https://github.com/user-attachments/assets/c650b4a5-0706-4393-978e-9690615ae95d" />


---

## 🗄️ MySQL Database Records

All generated URLs along with their click counts and timestamps are stored securely in the MySQL database.

<img width="807" height="371" alt="image" src="https://github.com/user-attachments/assets/bf87b27d-91a2-465a-b31b-89b9dcf73af1" />


---

## 📊 Database Information

| Field | Description |
|-------|-------------|
| Original URL | Stores the complete URL |
| Short URL | Stores generated short code |
| Click Count | Tracks total visits |
| Created At | Timestamp of creation |

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
```

---

### Navigate to the Project

```bash
cd url-shortener
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install Flask
pip install mysql-connector-python
pip install python-dotenv
```

or

```bash
pip install -r requirements.txt
```

---

### Create MySQL Database

```sql
CREATE DATABASE url_shortener;
```

---

### Create Table

```sql
CREATE TABLE url_mapping (
    id INT AUTO_INCREMENT PRIMARY KEY,
    long_url TEXT NOT NULL,
    short_url VARCHAR(20) UNIQUE,
    clicks INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### Configure Environment Variables

Create a `.env` file.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=url_shortener
```

---

### Run the Application

```bash
python app.py
```

---

Open your browser:

```
http://127.0.0.1:5000/
```

---

## 📈 Future Enhancements

- User Authentication
- QR Code Generation
- URL Analytics Dashboard
- Custom Short URLs
- Expiry Date for URLs
- Copy to Clipboard Button
- REST API Support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Shaik Fahad Jahangir**

GitHub:
https://github.com/Fahad7177-jeh

LinkedIn:
https://www.linkedin.com/in/shaik-fahad-jahangir-3746b92b6
