FROM fedora:30

COPY usr/. /usr/

RUN dnf install -y --setopt=tsflags=nodocs findutils procps which \
      glibc-langpack-en redhat-rpm-config gcc python3-devel python3-pip && \
    dnf clean -y --enablerepo='*' all && \
    sed -i.bak -e '1i auth requisite pam_deny.so' /etc/pam.d/su && \
    sed -i.bak -e 's/^%wheel/# %wheel/' /etc/sudoers && \
    useradd -u 1001 -g 0 -M -d /opt/app-root/src default && \
    mkdir -p /opt/app-root/src && \
    chown -R 1001:0 /opt/app-root && \
    fix-permissions /opt/app-root && \
    chmod g+w /etc/passwd

WORKDIR /opt/app-root/src

ENV HOME=/opt/app-root/src \
    PATH=/opt/app-root/src/bin:/opt/app-root/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8

USER 1001

COPY --chown=1001:0 opt/. /opt/

RUN python3 -m venv /opt/app-root/venv && \
    . /opt/app-root/venv/bin/activate && \
    pip3 install --no-cache-dir --upgrade pip setuptools wheel && \
    pip3 install --no-cache-dir /opt/app-root/src/requirements.txt \
    fix-permissions /opt/app-root

ENV BASH_ENV=/opt/app-root/etc/profile \
    ENV=/opt/app-root/etc/profile \
    PROMPT_COMMAND=". /opt/app-root/etc/profile"

ENTRYPOINT [ "container-entrypoint" ]

CMD [ "start-container" ]
