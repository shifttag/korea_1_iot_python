import src.service.webtoon as webtoon
import src.service.coupang as coupang
import src.service.kyobo as kyobo
import src.service.tms as tms
import src.repository.tms_repository as tmsRepository

def main():
    tms.run()

if __name__ == '__main__':
    main()