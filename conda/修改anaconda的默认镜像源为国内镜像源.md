## **修改anaconda的默认镜像源为国内镜像源**

Anaconda默认的镜像源大部分都是国外，国内很多网络环境下，访问不稳定，下载速率慢，有时候根本连接不上，另外国内也有镜像源，可以修改Anaconda的镜像源为国内，步骤如下：

1. 通过 `conda config` 命令配置

   .condarc文件的配置默认如下：

   ```tex
   ssl_verify: true
   channels:
     - defaults
   show_channel_urls: true
   ```

   .condarc文件一般在用户的家目录下（C:\Users\Administrator）。但是对应.condarc配置文件，是一种可选的，实在运行期配置的，期默认情况下是不存在的， Windows 用户无法直接创建名为 `.condarc` 的文件，可先执行 `conda config --set show_channel_urls yes` 生成该文件之后再修改。 

2. 在命令行或Anaconda Prompt中，输入`conda info`命令，查看默认配置的镜像源（channel URLS对应和配置文件路径config file）：

   ```powershell
   C:\Users\Administrator>conda info
   
        active environment : None
          user config file : C:\Users\Administrator\.condarc
    populated config files : C:\Users\Administrator\.condarc
             conda version : 4.7.12
       conda-build version : 3.18.9
            python version : 3.7.4.final.0
          virtual packages : __cuda=4.2
          base environment : D:\ProgramData\Anaconda3  (writable)
              channel URLs : https://repo.anaconda.com/pkgs/main/win-32
                             https://repo.anaconda.com/pkgs/main/noarch
                             https://repo.anaconda.com/pkgs/r/win-32
                             https://repo.anaconda.com/pkgs/r/noarch
                             https://repo.anaconda.com/pkgs/msys2/win-32
                             https://repo.anaconda.com/pkgs/msys2/noarch
             package cache : D:\ProgramData\Anaconda3\pkgs
                             C:\Users\Administrator\.conda\pkgs
                             C:\Users\Administrator\AppData\Local\conda\conda\pkgs
          envs directories : D:\ProgramData\Anaconda3\envs
                             C:\Users\Administrator\.conda\envs
                             C:\Users\Administrator\AppData\Local\conda\conda\envs
                  platform : win-32
                user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Windows/7 Windows/6.1.7601
             administrator : True
                netrc file : None
              offline mode : False
   
   ```

   

3. 修改默认镜像源为中科大的镜像源 https://mirrors.ustc.edu.cn/anaconda/pkgs/free 

   ```powershell
   conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
   conda config --set show_channel_urls yes
   ```

   

4. 查看==.condarc==配置文件，内容如下：

   ```tex
   ssl_verify: true
   channels:
     - https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
     - defaults
   ```

   ```powershell
   C:\Users\Administrator>conda info
   
        active environment : None
          user config file : C:\Users\Administrator\.condarc
    populated config files : C:\Users\Administrator\.condarc
             conda version : 4.7.12
       conda-build version : 3.18.9
            python version : 3.7.4.final.0
          virtual packages : __cuda=4.2
          base environment : D:\ProgramData\Anaconda3  (writable)
              channel URLs : https://mirrors.ustc.edu.cn/anaconda/pkgs/free/win-32
                             https://mirrors.ustc.edu.cn/anaconda/pkgs/free/noarch
                             https://repo.anaconda.com/pkgs/main/win-32
                             https://repo.anaconda.com/pkgs/main/noarch
                             https://repo.anaconda.com/pkgs/r/win-32
                             https://repo.anaconda.com/pkgs/r/noarch
                             https://repo.anaconda.com/pkgs/msys2/win-32
                             https://repo.anaconda.com/pkgs/msys2/noarch
             package cache : D:\ProgramData\Anaconda3\pkgs
                             C:\Users\Administrator\.conda\pkgs
                             C:\Users\Administrator\AppData\Local\conda\conda\pkgs
          envs directories : D:\ProgramData\Anaconda3\envs
                             C:\Users\Administrator\.conda\envs
                             C:\Users\Administrator\AppData\Local\conda\conda\envs
                  platform : win-32
                user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Windows/7 W
   indows/6.1.7601
             administrator : True
                netrc file : None
              offline mode : False
   ```

   

5. 执行`conda install pipenv`命令，验证配置是否成功

   ```powershell
   C:\Users\Administrator>conda install pipenv
   Collecting package metadata (current_repodata.json): failed
   
   CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://mirrors.ustc.edu.cn/
   anaconda/pkgs/free/win-32/current_repodata.json>
   Elapsed: -
   
   An HTTP error occurred when trying to retrieve this URL.
   HTTP errors are often intermittent, and a simple retry will get you on your way.
   
   SSLError(MaxRetryError('HTTPSConnectionPool(host=\'mirrors.ustc.edu.cn\', port=4
   43): Max retries exceeded with url: /anaconda/pkgs/free/win-32/current_repodata.
   json (Caused by SSLError("Can\'t connect to HTTPS URL because the SSL module is
   not available."))'))
   ```

   

6. 删除默认镜像源

   ```powershell
   conda config --remove channels defaults
   ```

   ```powershell
   C:\Users\Administrator>conda config --remove channels defaults
   
   C:\Users\Administrator>conda info
   
        active environment : None
          user config file : C:\Users\Administrator\.condarc
    populated config files : C:\Users\Administrator\.condarc
             conda version : 4.7.12
       conda-build version : 3.18.9
            python version : 3.7.4.final.0
          virtual packages : __cuda=4.2
          base environment : D:\ProgramData\Anaconda3  (writable)
              channel URLs : https://mirrors.ustc.edu.cn/anaconda/pkgs/free/win-32
                             https://mirrors.ustc.edu.cn/anaconda/pkgs/free/noarch
             package cache : D:\ProgramData\Anaconda3\pkgs
                             C:\Users\Administrator\.conda\pkgs
                             C:\Users\Administrator\AppData\Local\conda\conda\pkgs
          envs directories : D:\ProgramData\Anaconda3\envs
                             C:\Users\Administrator\.conda\envs
                             C:\Users\Administrator\AppData\Local\conda\conda\envs
                  platform : win-32
                user-agent : conda/4.7.12 requests/2.22.0 CPython/3.7.4 Windows/7 W
   indows/6.1.7601
             administrator : True
                netrc file : None
              offline mode : False
   ```

   

7. 1111