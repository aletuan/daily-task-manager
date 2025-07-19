# Daily Task Manager Web App

A modern, responsive web application for efficient daily task management with drag-and-drop functionality, priority-based organization, and real-time updates.

## 🚀 Features

- **Visual Task Board**: Drag-and-drop interface with columns for different task statuses
- **Priority Management**: Color-coded priority levels (Low, Medium, High)
- **Smart Organization**: Categorize tasks by project or context
- **Search & Filter**: Find tasks quickly with advanced search and filter options
- **Real-time Sync**: Automatic data persistence and synchronization
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **PostgreSQL**: Robust relational database
- **SQLAlchemy**: Python ORM for database operations
- **JWT**: Secure authentication

### Frontend
- **Streamlit**: Rapid Python-based web development
- **Custom Components**: Interactive drag-and-drop functionality
- **Responsive UI**: Modern, intuitive interface

### Infrastructure
- **Docker**: Containerized deployment
- **Redis**: Caching and session storage
- **GitHub Actions**: CI/CD pipeline

## 📋 Project Status

This project is currently in the planning phase. See the [Product Requirements Document](PRD_Daily_Task_Manager.md) for detailed specifications.

## 🎯 Roadmap

### Phase 1: MVP (4 weeks)
- [ ] Basic task CRUD operations
- [ ] Simple task board interface
- [ ] Database setup and basic API
- [ ] User authentication

### Phase 2: Enhanced Features (3 weeks)
- [ ] Drag-and-drop functionality
- [ ] Priority system and color coding
- [ ] Search and filter capabilities
- [ ] Responsive design implementation

### Phase 3: Polish and Launch (2 weeks)
- [ ] Performance optimization
- [ ] Security hardening
- [ ] User testing and feedback
- [ ] Production deployment

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL
- Docker (optional)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/daily-task-manager.git
cd daily-task-manager

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run the application
streamlit run app.py
```

## 📚 Documentation

- [Product Requirements Document](PRD_Daily_Task_Manager.md) - Comprehensive project specifications
- [API Documentation](docs/api.md) - Backend API reference
- [User Guide](docs/user-guide.md) - End-user documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- Create an issue for bugs or feature requests
- Email: support@dailytaskmanager.com
- Documentation: [docs/](docs/)

## 🙏 Acknowledgments

- FastAPI team for the excellent web framework
- Streamlit team for the amazing frontend framework
- PostgreSQL community for the robust database system

---

**Made with ❤️ for better task management** 