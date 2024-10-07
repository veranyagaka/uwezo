# Jukumu

**Jukumu** is a community-driven digital platform designed to empower citizens to report incidents of corruption and injustice, track the progress of their cases, view incident hotspots on a map, and support one another through donations. The platform fosters transparency, accountability, and collective action in fighting corruption and abuse of power.

## Features
- **Incident Reporting**: Users can report cases of corruption and injustice.
- **Progress Tracking**: Track the status and resolution of reported incidents.
- **Hotspot Mapping**: Visualize corruption and incident hotspots on a map.
- **Donation System**: Enable community members to support one another through donations.
- **Admin Verification**: Admins can approve and verify reported incidents for authenticity.
- **Anonymous Submissions**: Users can submit reports anonymously to protect their identity.

## Technologies Used
- **Frontend & Backend**: Django (Python)
- **Database**: MySQL
- **API**: M-Pesa API (for secure donations)
- **Authentication**: Django authentication system with admin approval features

## Installation

### Prerequisites
- Python 3.8+
- Django 3.0+
- MariaDB or MySQL
- Node (for Deployment)

### Setting Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/veranyagaka/jukumu.git
   cd jukumu
2. **Create a virtual environment**:
  ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```
3. **Install Dependencies**:
   Install the necessary Python dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the Database**:
   In settings.py, update the DATABASES section with your MariaDB/MySQL credentials:
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jukumu_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
   }
   ```
5. **Run Migrations**:
   Apply database migrations by running:
   ```bash
   python manage.py migrate
   ```
6. **Create a Superuser**:
   To create a superuser for accessing the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the Development Server**:
   Start the Django development server with the following command:
   ```bash
   python manage.py runserver
   ```
7. **M-Pesa Integration**:
   Jukumu integrates with the M-Pesa API to enable secure transactions for donations.
   
   1. Obtain your M-Pesa API credentials (sandbox or production).
   2. Add the necessary M-Pesa API keys in the environment variables:
      ```bash
      MPESA_CONSUMER_KEY=your_consumer_key
      MPESA_CONSUMER_SECRET=your_consumer_secret
      ```
## Usage
Incident Reporting: Users can report issues via the web interface. Admins will review and approve submissions.
Donations: Community members can contribute through M-Pesa to support victims of reported incidents.
Map: Incidents are displayed on a map, highlighting hotspots for corruption and injustice.

## Deployment
To deploy Jukumu on Render or any other service:

Set up environment variables (e.g., M-Pesa credentials, database credentials).
Install necessary dependencies and configure the production environment.
Deploy the Django project.

# Contributing
We welcome contributions to improve Jukumu. Please submit pull requests and ensure all tests pass before submitting.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, please reach out via [nyagakavera@gmail.com](mailto:nyagakavera@gmail.com) or follow us on social media:

- [Twitter: @JukumuApp](https://twitter.com/veranyagaka)
- [LinkedIn: Jukumu](https://www.linkedin.com/in/veranyagaka)

   


