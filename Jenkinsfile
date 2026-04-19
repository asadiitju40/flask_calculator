pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = "0"   // disable buildx requirement
    }

    stages {

        stage('Debug Environment') {
            steps {
                sh '''
                echo "=== Docker Info ==="
                docker --version

                echo "=== Docker Compose Info ==="
                docker-compose --version

                echo "=== Working Directory ==="
                pwd
                ls -la
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
                echo "=== Running Containers ==="
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
        always {
            echo "ℹ️ Pipeline execution finished"
        }
    }
}
