# 💼 Data Analytics Portfolio Website

A personal portfolio website built using **Django**, designed to showcase my **data analytics projects**, **skills**, **certifications**, and **experience**. This platform presents my journey into analytics in a professional format — helping recruiters and collaborators explore my work efficiently.

---

## 🚀 Features

- **Home Page** – Clean welcome section with dynamic navigation  
- **Projects Page** – Displays data analytics projects from the database (image, description, and link)  
- **About Me Page** – Includes name, date of birth, brief intro, education, certifications, work experience, and virtual internships  
- **Skills Page** – Lists tools and technologies like SQL, Power BI, Tableau, Excel, and Python  
- **Contact Page** – Contact details and external profile links  
- **Responsive Design** – Flexbox-based layout with hover effects  
- **Django Admin Integration** – Add/edit projects without modifying code  
- **Deployed Live on Render**

---

## 🛠 Tech Stack

| Layer       | Technology       |
|-------------|------------------|
| Backend     | Django (Python)  |
| Frontend    | HTML, CSS        |
| Database    | SQLite (Django ORM) |
| Deployment  | Render           |

---

## 📁 Project Structure

portfolio/ ├── manage.py ├── portfolio/ │ ├── settings.py │ ├── urls.py │ └── ... ├── app/ │ ├── models.py # Project model │ ├── views.py # Logic to fetch and display projects │ ├── templates/ │ │ ├── home.html │ │ ├── about.html │ │ ├── projects.html │ │ ├── skills.html │ │ └── contact.html │ ├── static/ │ │ └── style.css # Custom CSS styling


---

## 📊 Skills Highlighted

- SQL (PostgreSQL)  
- Power BI & Tableau  
- Data Cleaning & Modeling  
- Excel Automation  
- Python (beginner-level)  
- Django Web Framework  
- AI Prompt Engineering  

---

## 🧠 What I Learned

- Django framework structure: Models, Views, Templates  
- Handling static and media files  
- Dynamic content rendering using Django ORM  
- Styling with Flexbox and managing layout issues  
- Admin panel customization  
- Hosting Django websites using Render  
- Debugging common deployment issues (e.g., static file not loading)

---

## 🐞 Challenges Faced

- Static files not loading on Render → fixed by checking `STATIC_URL` & `STATICFILES_DIRS`  
- Page responsiveness → resolved using `flex-wrap` and `media queries`  
- Project duplication in admin → fixed by cleaning the database  
- Deployment errors due to missing `.env` and `allowed_hosts`

---

## 📍 Based in Kerala, India

I built this project as a Data Analyst transitioning from a Sales background, aiming to land impactful roles by showcasing practical skills in a professional setting.

---

## 🌐 Live Website

🚀 [View My Portfolio on Render](https://data-analytics-portfolio-rjif.onrender.com)

---

## 📬 Contact

- 📍 Location: Kerala, India  
- 📧 Email: nmakhila2709@gmail.com  
- 🔗 [LinkedIn](https://www.linkedin.com/in/akhila-nm-0b890b339/)  
- 💻 [GitHub](https://github.com/akhilanm123)

---



## 🙌 Acknowledgements

- Django Documentation  
- Stack Overflow & ChatGPT  
- Render Hosting Docs  
- GitHub README best practices
