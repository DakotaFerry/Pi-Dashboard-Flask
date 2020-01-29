function dockerip() {
docker ps | tail -n +2 | while read cid b; do echo -n "$cid\t"; docker inspect $cid | grep IPAddress | cut -d \" -f 4; done
}

dockerip #| grep "^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(?!$)|$)){4}$"

