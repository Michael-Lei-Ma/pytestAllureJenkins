pipeline {
    agent any

    // 定义全局工具（如 Allure，需先在 Jenkins 全局工具中配置）
    tools {
        allure 'allure'   // 名称必须与 Jenkins 全局工具配置中的 Allure 名称一致
    }

    environment {
        // 如果你的 Python 不在 PATH 中，可以指定绝对路径（可选）
        PYTHON = 'D:\\360software\\python313\\python.exe'
        // 项目虚拟环境目录（可选）
        // VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // 从 Git 仓库拉取代码（自动使用 Jenkins 任务中配置的 SCM）
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                    if not exist %VENV_DIR% ( %PYTHON% -m venv %VENV_DIR% )
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests with Pytest and Allure') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    pytest tests/ --alluredir=allure-results
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                // 生成并发布 Allure 报告（需安装 Allure Jenkins Plugin）
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

        stage('Deploy (Optional)') {
            when {
                // 仅当分支为 main 且测试全部通过时执行
                branch 'master'
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                bat 'xcopy /E /I /Y src\\* D:\\deploy\\my_app\\'
                // 或者执行其他部署命令（如重启服务）
            }
        }
    }

    post {
        always {
            // 无论成功或失败都清理工作空间（可选，需安装 Workspace Cleanup 插件）
            cleanWs()
            echo 'Pipeline finished.'
        }
    }
}