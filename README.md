# 🎓 Alumni Information System

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
</div>

<p align="center">
  <strong>A comprehensive command-line application for managing alumni information with CRUD operations and automatic data generation.</strong>
</p>

## 📋 Table of Contents
- [Features](#-features)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Code Structure](#-code-structure)
- [Data Validation](#-data-validation)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🔧 Core Functionality
- **Add Alumni Data**: Manually input new alumni information with validation
- **Check Alumni Details**: Search and view specific alumni information
- **Update Alumni Data**: Modify existing contact information, email, occupation, and address
- **Delete Alumni Data**: Remove alumni records from the system
- **List All Alumni**: Display all registered alumni with complete details

### 🤖 Smart Features
- **Automatic Data Generation**: Generates 5-10 random alumni records if database has less than 5 entries
- **Input Validation**: Ensures data integrity with email and phone number validation
- **Pre-loaded Sample Data**: Comes with 3 sample alumni records for immediate testing

### 📊 Data Management
- **Unique Identification**: Each alumni has a unique 5-digit admission number
- **Comprehensive Records**: Stores name, admission/graduation years, contact info, occupation, and address
- **Data Persistence**: Maintains data throughout the session

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses built-in libraries only)

### Installation

1. **Clone the repository**
git clone https://github.com/yourusername/alumni-information-system.git
cd alumni-information-system


2. **Run the application**

## 📖 Usage

### Main Menu Options

Welcome to the Alumni Information System

Options:

Add Alumni Data # Add new alumni records

Check Alumni Details # Search for specific alumni

Update Alumni Data # Modify existing records

Delete Alumni Data # Remove alumni records

List All Alumni # View all alumni

Exit # Close the application


## 🏗️ Code Structure
**alumni_system.py
├── Data Validation Functions
│ ├── is_valid_contact() # Validates 10-digit phone numbers
│ └── is_valid_email() # Validates email format
├── Core CRUD Operations
│ ├── add_alumni_data() # Create new records
│ ├── check_alumni_details() # Read existing records
│ ├── update_alumni_data() # Update records
│ └── delete_alumni_data() # Delete records
├── Utility Functions
│ ├── generate_random_alumni() # Auto-generate sample data
│ └── list_all_alumni() # Display all records
└── main() # Main application loop**

## 🔍 Data Validation

### Contact Number Validation
- Must be exactly 10 digits
- Only numeric characters allowed
- Example: `9876543210` ✅ `98765432` ❌

### Email Validation
- Must contain `@` symbol
- Must contain at least one `.` (dot)
- Example: `user@example.com` ✅ `userexample.com` ❌

### Admission Number Validation
- Must be exactly 5 digits
- Automatically checked for uniqueness
- Example: `12345` ✅ `1234` ❌

## 📊 Sample Data Structure

alumni = {
"10345": {
'Name': 'John Doe',
'Year of Admission': 2010,
'Year of Graduation': 2014,
'Contact No.': '1234567890',
'E-mail Address': 'john@example.com',
'Occupation': 'Software Engineer',
'Address': '123 Elm St'
}
}
5. **Open a Pull Request**

### 💡 Ideas for Contribution
- Add data persistence (JSON/CSV file storage)
- Implement search by name or graduation year
- Add data export functionality
- Create a GUI version using Tkinter
- Add alumni statistics and analytics

## 🐛 Known Issues & Future Enhancements

### Current Limitations
- Data is not persistent across sessions
- Limited search functionality
- No data backup/restore feature

### Planned Features
- [ ] File-based data persistence
- [ ] Advanced search filters
- [ ] Data import/export (CSV, JSON)
- [ ] Alumni statistics dashboard
- [ ] Email notification system
- [ ] GUI interface

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Contact: [abhinav.is.av@gmail.com]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">
<p>Made with ❤️ for educational purposes</p>
<p>⭐ Star this repository if you found it helpful!</p>
</div>
