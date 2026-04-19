pipeline {
    agent any

    environment {
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {

        stage('Debug Environment') {
            steps {
                sh '''
                echo "Checking Docker & Compose..."
                docker --version
                docker-compose --version
                '''
            }
        }

        stage('Stop Existing Stack') {
            steps {
                sh '''
                docker-compose down || true
                '''
            }
        }

        stage('Build & Start Services') {
            steps {
                sh '''
                docker-compose up -d --build
                '''
            }
        }

        stage('Verify Running Containers') {
            steps {
                sh '''
                docker ps
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Full stack deployed successfully (Flask + Monitoring)"
            echo "🌐 Access app: http://<your-server-ip>:5000"
        }
        failure {
            echo "❌ Build or deployment failed"
        }
    }
}
