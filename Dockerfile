# 配置基础镜像
FROM alpine

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories

# 更新升级软件
RUN apk add --update --upgrade

# 安装软件
RUN apk add --no-cache python3

# 升级pip，这一步同时会在/usr/bin/目录下生成pip可执行文件
RUN pip3 install -i  https://pypi.tuna.tsinghua.edu.cn/simple some-package --no-cache-dir --upgrade pip

# 建立软链接
RUN ln -s /usr/bin/python3 /usr/bin/python

# 创建工作路径
RUN mkdir /app

# 指定容器启动时执行的命令都在app目录下执行
WORKDIR /app

# 将本地app目录下的内容拷贝到容器的app目录下
COPY ./app/ /app/

# pip读取requirements.txt内容安装所需的库
RUN pip install -r /app/requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple some-package --no-cache-dir

# 启动nginx和uwsgi
ENTRYPOINT python /app/app.py