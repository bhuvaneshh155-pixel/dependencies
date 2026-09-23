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
            
                bat 'if exist app.py del app.py'
                bat 'if exist test_app.py del test_app.py'

        
                bat '''
                (
                echo def find_min(numbers^):
                echo     if not numbers: return None
                echo     return min(numbers^)
                echo def count_odds(numbers^):
                echo     return sum(1 for x in numbers if x %% 2 != 0^)
                ) > app.py
                '''

                
                bat '''
                (
                echo import pytest
                echo from app import find_min, count_odds
                echo @pytest.mark.parametrize("numbers, expected", [
                echo     ([10, 20, 30], 10^),
                echo     ([-1, -5, 0, 2], -5^),
                echo     ([7], 7^),
                echo     ([10, 20, 30], 99^)
                echo ])
                echo def test_find_min(numbers, expected^):
                echo     assert find_min(numbers^) == expected
                echo @pytest.mark.parametrize("numbers, expected", [
                echo     ([1, 2, 3, 4, 5], 3^),
                echo     ([2, 4, 6, 8], 0^),
                echo     ([1, 3, 5, 7], 4^)
                echo ])
                echo def test_count_odds(numbers, expected^):
                echo     assert count_odds(numbers^) == expected
                ) > test_app.py
                '''

            
                bat '''
                    if not exist venv (
                        python -m venv venv
                    )
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest -v
                '''
            }
        }
    }
}
