# Linux / macOS で./manage.py runserverのように 直接実行できるようにする指定
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # 設定ファイルの読み込み
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Django のコマンド実体を読み込む
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
