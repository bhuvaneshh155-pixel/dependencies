pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                
                
                sh '''
                    echo "=== Checking Python Environment ==="
                    python3 --version || python --version
                    
                    echo "=== Creating Virtual Environment ==="
                    python3 -m venv venv || python -m venv venv
                    
                    echo "=== Installing Dependencies ==="
                    . venv/bin/activate || ./venv/Scripts/activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate || ./venv/Scripts/activate
                    pytest -v
                '''
            }
        }
    }
}
