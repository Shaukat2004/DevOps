pipeline {
  agent any

  stages {
    stage('Install Dependencies') {
      steps {
        bat 'pip install -r requirements.txt'
      }
    }
    stage('Migrate Database') {
      steps {
        bat 'python manage.py migrate'
      }
    }
    stage('Run Tests') {
      steps {
        bat 'python manage.py test'
      }
    }
  }
}
