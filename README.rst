gitts - Git Time Shift
======================

gitts is a Python script that allows you to execute Git commands with a time offset applied to the commit timestamp. This enables you to create commits in the past or future.

`日本語版はこちら`_

Usage
-----

::

  gitts <offset_minutes> <git_command> [<git_arguments>...]

- ``offset_minutes``: The time offset in minutes to apply to the commit timestamp. Positive values represent the future, while negative values represent the past.

- ``git_command``: The Git command to execute (e.g., ``commit``, ``rebase``, etc.).

- ``git_arguments``: Additional arguments to pass to the Git command.

Examples
~~~~~~~~

::

  gitts 30 commit -m "Future commit"

The above command creates a commit with the message "Future commit" and sets the commit timestamp to 30 minutes in the future.

::

  gitts -60 rebase -i HEAD~5

The above command performs an interactive rebase of the last 5 commits with the commit timestamp set to 60 minutes in the past.

Installation
------------

1. Place ``gitts.py`` in a location of your choice.

2. Grant execute permissions to the script:

   ::

     chmod +x /path/to/gitts.py

3. Make the script executable using one of the following methods:
   
   a. Create a symbolic link named ``gitts`` to the script in a directory that is in your PATH:

      ::

        ln -s /path/to/gitts.py /usr/local/bin/gitts

   b. If using an alias, add the following line to your shell configuration file (e.g., ``.bashrc``, ``.zshrc``, etc.):

      ::

        alias gitts='/path/to/gitts.py'

Now you can execute the script using the ``gitts`` command.

Notes
-----

- gitts modifies the commit timestamp by setting the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables. These environment variables are only effective within the process where gitts is invoked.

- Modifying the commit timestamp alters the history of the repository. Use caution, especially when working with shared repositories.

- Significant changes to the timestamp may compromise the integrity of the repository. It is recommended to use moderate time offsets.

License
-------

Copyright 2024 Yumeto Inaoka

gitts is licensed under the Apache License 2.0. For more information, see the LICENSE file.

----

.. _`日本語版はこちら`:

gitts - Git Time Shift
======================

gitts は、コミットのタイムスタンプに時間オフセットを適用して Git コマンドを実行する Python スクリプトです。これにより、過去または未来の日時でコミットを作成できます。

使い方
------

::

  gitts <offset_minutes> <git_command> [<git_arguments>...]

- ``offset_minutes``: コミットタイムスタンプに適用する時間オフセット（分単位）。正の値は未来、負の値は過去を表します。

- ``git_command``: 実行するGitコマンド（例: ``commit``、``rebase``など）。

- ``git_arguments``: Gitコマンドに渡す追加の引数。

例
~~

::

  gitts 30 commit -m "Future commit"

上記のコマンドは、現在時刻の30分後にコミットタイムスタンプを設定して、"Future commit"というメッセージでコミットを作成します。

::

  gitts -60 rebase -i HEAD~5

上記のコマンドは、現在時刻の60分前にコミットタイムスタンプを設定して、直前の5つのコミットを対話的にリベースします。

インストール
------------

1. ``gitts.py``をお好みの場所に配置します。

2. スクリプトに実行権限を付与します：

   ::

     chmod +x /path/to/gitts.py

3. 以下のいずれかの方法でスクリプトを実行可能にします：
   
   a. パスの通ったディレクトリに、``gitts``という名前でスクリプトのシンボリックリンクを作成します：

      ::

        ln -s /path/to/gitts.py /usr/local/bin/gitts

   b. エイリアスを使用する場合は、シェルの設定ファイル（例: ``.bashrc``、``.zshrc``など）に以下の行を追加します：

      ::

        alias gitts='/path/to/gitts.py'

これで、``gitts``コマンドを使用してスクリプトを実行できるようになります。

注意事項
--------

- gittsは、GIT_AUTHOR_DATEとGIT_COMMITTER_DATE環境変数を設定することで、コミットタイムスタンプを変更します。これらの環境変数は、gittsが呼び出されたプロセス内でのみ有効です。

- コミットタイムスタンプを変更すると、リポジトリの履歴が変更されます。特に共有リポジトリでは注意して使用してください。

- 大幅なタイムスタンプの変更は、リポジトリの整合性を損なう可能性があります。適度な時間オフセットを使用することをお勧めします。

ライセンス
----------

Copyright 2024 Yumeto Inaoka

gitts は Apache License 2.0 の下でライセンスされています。詳細については LICENSE ファイルを参照してください。
