# InvoiceIQ

> Transform invoices into structured data in seconds using AI.

InvoiceIQ is an AI-powered invoice processing platform that automates invoice data extraction from PDFs and images. It leverages Google Gemini Flash to extract structured information, stores processed invoices in Supabase, and provides a validation workflow that allows users to review and correct AI-generated data.

---

## ✨ Features

- 🔐 User Authentication
- 📄 Upload invoice PDFs and images
- 🤖 AI-powered data extraction using Gemini Flash
- 🏢 Extract vendor details
- 🧾 Extract GSTIN
- 📅 Extract invoice dates
- 💰 Extract invoice totals
- ⚠️ Flag potentially incorrect fields
- ✏️ Edit extracted information
- ☁️ Store processed invoices in Supabase
- 📊 Clean dashboard for invoice management

---

## 🛠 Tech Stack

### Frontend
- React
- Tailwind CSS

### Backend
- Node.js
- Express.js

### AI
- Google Gemini Flash

### Database
- Supabase

---

## 🏗 Architecture

Invoice Upload
        ↓
 PDF / Image Processing
        ↓
 Gemini Flash
        ↓
 Structured JSON
        ↓
 Validation Layer
        ↓
 Supabase
        ↓
 Dashboard

---

## 📸 Screenshots

### Login
<img width="1917" height="1027" alt="Screenshot 2026-07-31 125422" src="https://github.com/user-attachments/assets/dee4a0b4-e977-41cf-b509-debc083de7ab" />

### Dashboard
<img width="1716" height="917" alt="ChatGPT Image Jul 31, 2026, 01_08_04 PM" src="https://github.com/user-attachments/assets/ddb6097c-7d65-48e7-bb75-d3c38873bcd5" />
### Invoice Upload
<img width="1718" height="916" alt="ChatGPT Image Jul 31, 2026, 01_13_48 PM" src="https://github.com/user-attachments/assets/7eaff68d-f5ea-4eac-8933-b73dd9c89fb8" />



### Extracted Results

<img width="1097" height="902" alt="Screenshot 2026-07-31 130602" src="https://github.com/user-attachments/assets/c6991d50-5a4c-4444-af61-dec897eb9ddf" />


---

## 🚀 Getting Started

### Clone Repository

```bash
git clone <repo-link>
```

### Install Dependencies

```bash
npm install
```

### Configure Environment Variables

```env
GEMINI_API_KEY=
SUPABASE_URL=
SUPABASE_ANON_KEY=
```

### Run

```bash
npm run dev
```

---

## 🎯 Future Improvements

- Batch invoice processing
- Multi-language invoice support
- Export to Excel
- Confidence score visualization
- Role-based access control
- Analytics dashboard

---

## 👨‍💻 Author

**Sumukh Suresh**

LinkedIn: www.linkedin.com/in/sumukhsureshcs

GitHub: github/Sumukh298
