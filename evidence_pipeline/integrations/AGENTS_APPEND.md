# 통합할 카드뉴스 운영 블록
아래 BEGIN/END 내부를 프로젝트 AGENTS.md의 카드뉴스 규칙에 통합한다.
이 파일은 독립 실행 에이전트 설정 파일이 아니다.

<!-- BEGIN R_SPORTS_EVIDENCE_PIPELINE -->
## 카드뉴스: 근거와 내용 확정 후 제작
카드뉴스 작업은 `evidence_pipeline/README.md`와 `evidence_pipeline/WORKFLOW.md`를 읽고 수행한다.
기본 흐름은 사용자 의견 → 연구/주장 검증 → Research Brief → 카드별 문안 → 사용자 내용 확정 → 디자인/개별 PNG/검수다.
‘[주제] 카드뉴스 만들어줘’만 받으면 기본적으로 카드별 문안 전체까지 만들고 내용 확인을 요청한다. 디자인 취향·기존 크기·브랜딩은 재질문하지 않는다.
사용자가 이미 이번 작업에서 디자인까지 명확히 허용했다면 그 범위를 기록하고 반복 확인 없이 진행한다.
`content/<slug>/`의 brief.md, user_notes.md, research/sources.md, research/claims.md, research/research_brief.md, research/evidence_review.md, storyboard.md, approval_log.md를 사용한다.
근거에 없는 의학적 주장·수치·처방·검사 기준을 추가하지 않는다. 사용자 필수 의견도 근거 검증한다.
새로운 의학적 내용을 추가할 때만 영향받는 근거와 문안을 갱신한다. 오타·줄바꿈·뜻이 같은 편집은 재확정 없이 진행한다.
기존 DESIGN_SYSTEM.md와 references/의 디자인 규칙은 제작 단계에서 유지한다.
roles/의 문서는 역할 지침이다. 기본은 한 에이전트가 순차 수행하며, 파일 생성만으로 다중 에이전트가 설치되었다고 말하지 않는다.
다른 마케팅 업무·CRM·매출·개인정보 경계를 변경하지 않는다.
<!-- END R_SPORTS_EVIDENCE_PIPELINE -->

## 기존 V2에서 함께 수정할 충돌 문구
- 서두의 ‘주제 한 문장만 받아도 기본 제작 과정을 실행’ → ‘주제 한 문장으로 카드별 문안까지, 내용 확정 후 디자인’
- 역할 설명의 ‘자료 조사 → … → 6장 PNG를 기본 실행’ → WORKFLOW.md의 단계
- 기본값 표의 ‘출력’은 최종 제작 단계 출력임을 명시
- 근거에 관한 기존 rules는 삭제하지 않고 새 기록 방식에 연결
- 기존 파일 계약에 추가 research_brief/evidence_review/user_notes/approval_log 포함
단순 맨 아래 추가로 상충 지침을 남겨두지 않는다. 현재 실제 파일이 V2와 다르면 의도를 보존해 해당 구절만 수정한다.
