# 00 — 기존 Codex 프로젝트에 처음 연결하기
사용 위치: 기존 카드뉴스/AI 마케팅팀 프로젝트를 연 Codex.
먼저 evidence_pipeline/ 폴더를 프로젝트 루트에 복사한다.
아래 실행 프롬프트 전체를 복사한다.

## 실행 프롬프트
현재 프로젝트의 카드뉴스 작업에 evidence_pipeline 운영 방식을 실제로 통합해줘.

1. 현재 프로젝트 루트와 기존 AGENTS.md, CARDNEWS_WORKFLOW.md, DESIGN_SYSTEM.md를 확인해줘. evidence_pipeline/README.md, WORKFLOW.md, integrations/의 두 파일을 읽어줘.
2. 기존 파일이 없거나 다른 구조라면 확인한 경로를 보고하고 현재 실제 파일에 맞춰 연결해줘. 존재하지 않는 파일을 읽었다고 하지 마.
3. 수정 전 원본 AGENTS.md와 CARDNEWS_WORKFLOW.md를 backups/evidence-install/<실제 시각>/에 보관해줘. 기존 백업은 덮어쓰지 마.
4. AGENTS.md의 카드뉴스 관련 규칙에 integrations/AGENTS_APPEND.md의 BEGIN/END 블록을 한 번만 통합해줘. 같은 블록이 있다면 중복 삽입하지 말고 이번 버전과 차이를 반영해줘.
5. ‘주제 한 줄이면 조사부터 PNG까지 기본 실행’처럼 새 흐름과 충돌하는 카드뉴스 문구를 ‘카드별 문안까지 먼저, 사용자 내용 확정 후 디자인’으로 고쳐줘. 맨 아래 블록만 추가해 모순을 남기지 마.
6. CARDNEWS_WORKFLOW.md에 integrations/CARDNEWS_WORKFLOW_PATCH.md의 연결을 반영해줘. 소재 제작과 렌더링은 기본적으로 내용 확정 다음 단계야.
7. 사용자 요청에 이미 디자인까지 진행할 권한이 있으면 형식적인 재확인을 반복하지 않도록 예외도 연결해줘.
8. DESIGN_SYSTEM.md와 references/의 이미지·폰트·CSS·디자인은 유지해줘. 다른 업무의 에이전트 설정, 개인정보 경계, CRM·매출 업무는 수정하지 마.
9. 이 폴더의 roles/는 읽어 사용하는 역할 지침이야. 실제 별도 에이전트 설정이나 검색/이미지 권한을 설치했다고 말하지 마.
10. 통합 뒤 관련 문구를 검색해 충돌과 중복을 점검하고, 실제 변경 파일·백업 위치·최종 기본 진행 단계만 보고해줘.

지금은 설치·연결만 수행하고 카드뉴스는 만들지 마.
