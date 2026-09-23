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
                // 1. Wipe out any broken or locked test scripts from prior runs
                bat 'if exist app.py del app.py'
                bat 'if exist test_app.py del test_app.py'

                // 2. Generate clean application logic (app.py)
                bat 'echo def find_min(numbers): > app.py'
                bat 'echo     if not numbers: return None >> app.py'
                bat 'echo     return min(numbers) >> app.py'
                bat 'echo def count_odds(numbers): >> app.py'
                bat 'echo     return sum(1 for x in numbers if x %% 2 != 0) >> app.py'

                // 3. Generate the test verification suite (test_app.py)
                bat 'echo import pytest > test_app.py'
                bat 'echo from app import find_min, count_odds >> test_app.py'
                
                // Add the 4 parametric cases for find_min (3 valid + 1 intentional failure)
                bat 'echo @pytest.mark.parametrize("numbers, expected", [ >> test_app.py'
                bat 'echo     ([1, 2, 3], 1), >> test_app.py'
                bat 'echo     ([-1, -5, 0, 2], -5), >> test_app.py'
                bat 'echo     ([7], 7), >> test_app.py'
                bat 'echo     ([10, 20, 30], 99) >> test_app.py' 
                bat 'echo ]) >> test_app.py'
                bat 'echo def test_find_min(numbers, expected): >> test_app.py'
                bat 'echo     assert find_min(numbers) == expected >> test_app.py'
                
                // Add the 3 parametric cases for count_odds
                bat 'echo @pytest.mark.parametrize("numbers, expected", [ >> test_app.py'
                bat 'echo     ([1, 2, 3, 4, 5], 3), >> test_app.py'
                bat 'echo     ([2, 4, 6], 0), >> test_app.py'
                bat 'echo     ([1, 3, 5, 7], 4) >> test_app.py'
                bat 'echo ]) >> test_app.py'
                bat 'echo def test_count_odds(numbers, expected): >> test_app.py'
                bat 'echo     assert count_odds(numbers) == expected >> test_app.py'

                // 4. Safely set up or reuse the virtual environment
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
                // 5. Run the tests while keeping the command prompt process clear and responsive
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest -v
                '''
            }
        }
    }
}
