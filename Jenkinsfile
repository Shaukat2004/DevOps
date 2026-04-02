pipeline {
  agent any

  stages {

    stage('Run Tests in Docker') {
      steps {
        bat 'docker run --rm budget-tracker-app:1.0 python manage.py test'
      }
    }

  }
}
