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
                // 1. Generate the core application logic (app.py)
                bat 'echo def find_min(numbers): > app.py'
                bat 'echo     if not numbers: return None >> app.py'
                bat 'echo     return min(numbers) >> app.py'
                bat 'echo def count_odds(numbers): >> app.py'
                bat 'echo     return sum(1 for x in numbers if x %% 2 != 0) >> app.py'

                // 2. Generate the parametric validation test file (test_app.py)
                bat 'echo import pytest > test_app.py'
                bat 'echo from app import find_min, count_odds >> test_app.py'
                
                // Add the 4 test cases for find_min (3 valid + 1 intentional failure)
                bat 'echo @pytest.mark.parametrize("numbers, expected", [ >> test_app.py'
                bat 'echo     ([1, 2, 3, 4, 5], 1), >> test_app.py'
                bat 'echo     ([-1, -5, 0, 2], -5), >> test_app.py'
                bat 'echo     ([7], 7), >> test_app.py'
                bat 'echo     ([10, 20, 30], 99) >> test_app.py' // Intentional failure case
                bat 'echo ]) >> test_app.py'
                bat 'echo def test_find_min(numbers, expected): >> test_app.py'
                bat 'echo     assert find_min(numbers) == expected >> test_app.py'
                
                // Add the 3 test cases for count_odds
                bat 'echo @pytest.mark.parametrize("numbers, expected", [ >> test_app.py'
                bat 'echo     ([1, 2, 3, 4, 5], 3), >> test_app.py'
                bat 'echo     ([2, 4, 6, 8], 0), >> test_app.py'
                bat 'echo     ([1, 3, 5, 7], 4) >> test_app.py'
                bat 'echo ]) >> test_app.py'
                bat 'echo def test_count_odds(numbers, expected): >> test_app.py'
                bat 'echo     assert count_odds(numbers) == expected >> test_app.py'

                // 3. Provision the Python virtual sandbox environment and dependencies
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // 4. Initialize virtual environment and execute verification
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest -v
                '''
            }
        }
    }
}
