pipeline {
    agent { docker { image 'python:3.6.3' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'behave'
                sh 'pytest'
            }
        }
    }
}

