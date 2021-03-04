CREATE TABLE tb_QuestionGroupFormRecord (
  questionGroupFormRecordID SERIAL NOT NULL, 
  formRecordID              int4 NOT NULL, 
  crfFormsID                int4 NOT NULL, 
  questionID                int4 NOT NULL, 
  listOfValuesID            int4, 
  answer                    varchar(512), 
  PRIMARY KEY (questionGroupFormRecordID));
COMMENT ON TABLE tb_QuestionGroupFormRecord IS '(pt-br) Tabela para registro da resposta associada a uma questão de um agrupamento de um formulário referente a um questionario de avaliação.
(en) Form record table.';
CREATE TABLE tb_AssessmentQuestionnaire (
  participantID   varchar(50) NOT NULL, 
  hospitalUnitID  int4 NOT NULL, 
  questionnaireID int4 NOT NULL, 
  PRIMARY KEY (participantID, 
  hospitalUnitID, 
  questionnaireID));
COMMENT ON COLUMN tb_AssessmentQuestionnaire.participantID IS '(pt-br)  Chave estrangeira para a tabela tb_Patient.
(en) Foreign key to the tb_Patient table.';
COMMENT ON COLUMN tb_AssessmentQuestionnaire.hospitalUnitID IS '(pt-br) Chave estrangeira para tabela tb_HospitalUnit.
(en) Foreign key for the tp_HospitalUnit table.';
CREATE TABLE tb_Participant (
  participantID varchar(50) NOT NULL, 
  medicalRecord varchar(255) NOT NULL, 
  PRIMARY KEY (participantID));
COMMENT ON TABLE tb_Participant IS '(pt-br) Tabela para registros de pacientes.
(en) Table for patient records.';
COMMENT ON COLUMN tb_Participant.medicalRecord IS '(pt-br) prontuário do paciente. 
(en) patient medical record.';
CREATE TABLE tb_HospitalUnit (
  hospitalUnitID   SERIAL NOT NULL, 
  hospitalUnitName varchar(500) NOT NULL, 
  PRIMARY KEY (hospitalUnitID));
COMMENT ON TABLE tb_HospitalUnit IS '(pt-br) Tabela para identificação de unidades hospitalares.
(en) Table for hospital units identification.';
COMMENT ON COLUMN tb_HospitalUnit.hospitalUnitName IS '(pt-br) Nome da unidade hospitalar.
(en) Name of the hospital unit.';
CREATE TABLE tb_ListType (
  listTypeID  SERIAL NOT NULL, 
  description varchar(255) NOT NULL, 
  PRIMARY KEY (listTypeID));
COMMENT ON COLUMN tb_ListType.description IS '(pt-br) Descrição.
(en) description.';
CREATE TABLE tb_QuestionType (
  questionTypeID SERIAL NOT NULL, 
  description    varchar(255) NOT NULL, 
  CONSTRAINT questionTypeID 
    PRIMARY KEY (questionTypeID));
COMMENT ON COLUMN tb_QuestionType.description IS '(pt-br) Descrição.
(en) description.';
CREATE TABLE tb_QuestionGroup (
  questionGroupID SERIAL NOT NULL, 
  description     varchar(255) NOT NULL, 
  comment         varchar(255), 
  PRIMARY KEY (questionGroupID));
COMMENT ON TABLE tb_QuestionGroup IS 'Relacionado ao Question Group da ontologia relaciona as diversas sessoes existentes nos formularios do CRF COVID-19';
COMMENT ON COLUMN tb_QuestionGroup.description IS '(pt-br) Descrição.
(en) description.';
CREATE TABLE tb_ListOfValues (
  listOfValuesID SERIAL NOT NULL, 
  listTypeID     int4 NOT NULL, 
  description    varchar(255) NOT NULL, 
  PRIMARY KEY (listOfValuesID));
COMMENT ON TABLE tb_ListOfValues IS '(pt-br) Representa todos os valores padronizados do formulário.
(en) Represents all standard values on the form.';
COMMENT ON COLUMN tb_ListOfValues.description IS '(pt-br) Descrição.
(en) description.';
CREATE TABLE tb_CRFForms (
  crfFormsID      SERIAL NOT NULL, 
  questionnaireID int4 NOT NULL, 
  description     varchar(255) NOT NULL, 
  PRIMARY KEY (crfFormsID));
COMMENT ON TABLE tb_CRFForms IS '(pt-br)
tb_CRFForms identifica o tipo do formulario refere-se ao Questionnaire Subsection da Ontologia:
Admissão - Modulo 1
Acompanhamento - Modulo 2
Desfecho - Modulo 3
(en)
tb_CRFForms identifies the type of the form refers to the Questionnaire Subsection of Ontology: Admission - Module 1 Monitoring - Module 2 Outcome - Module 3';
COMMENT ON COLUMN tb_CRFForms.description IS '(pt-br) Descrição .
(en) description.';
CREATE TABLE tb_Questions (
  questionID      SERIAL NOT NULL, 
  description     varchar(255) NOT NULL, 
  questionTypeID  int4 NOT NULL, 
  listTypeID      int4, 
  questionGroupID int4, 
  subordinateTo   int4, 
  isAbout         int4, 
  PRIMARY KEY (questionID));
COMMENT ON COLUMN tb_Questions.description IS '(pt-br) Descrição.
(en) description.';
COMMENT ON COLUMN tb_Questions.questionTypeID IS '(pt-br) Chave estrangeira para tabela tb_QuestionsTypes.
(en) Foreign key for the tp_QuestionsTypes table.';
CREATE TABLE tb_Questionnaire (
  questionnaireID SERIAL NOT NULL, 
  description     varchar(255) NOT NULL, 
  PRIMARY KEY (questionnaireID));
CREATE TABLE tb_QuestionGroupForm (
  crfFormsID    int4 NOT NULL, 
  questionID    int4 NOT NULL, 
  questionOrder int4 NOT NULL, 
  PRIMARY KEY (crfFormsID, 
  questionID));
CREATE TABLE tb_FormRecord (
  formRecordID    SERIAL NOT NULL, 
  participantID   varchar(50) NOT NULL, 
  hospitalUnitID  int4 NOT NULL, 
  questionnaireID int4 NOT NULL, 
  crfFormsID      int4 NOT NULL, 
  dtRegistroForm  timestamp NOT NULL, 
  PRIMARY KEY (formRecordID));
CREATE TABLE tb_Ontology (
  ontologyID  SERIAL NOT NULL, 
  description varchar(255) NOT NULL, 
  version     varchar(255) NOT NULL, 
  dtRelease   timestamp, 
  license     varchar(255) NOT NULL, 
  acronym     varchar(255) NOT NULL, 
  PRIMARY KEY (ontologyID));
CREATE TABLE tb_OntologyTerms (
  ontologyURI varchar(255) NOT NULL, 
  ontologyID  int4 NOT NULL, 
  termTypeID  int4 NOT NULL, 
  description varchar(255), 
  PRIMARY KEY (ontologyURI));
CREATE TABLE tb_QuestionnaireParts (
  questionnairePartsID      int4 NOT NULL, 
  questionnairePartsTableID int4 NOT NULL, 
  PRIMARY KEY (questionnairePartsID, 
  questionnairePartsTableID));
CREATE TABLE tb_QuestionnairePartsTable (
  questionnairePartsTableID SERIAL NOT NULL, 
  description               varchar(255) NOT NULL, 
  PRIMARY KEY (questionnairePartsTableID));
CREATE TABLE tb_QuestionnairePartsOntology (
  ontologyURI               varchar(255) NOT NULL, 
  questionnairePartsID      int4 NOT NULL, 
  questionnairePartsTableID int4 NOT NULL, 
  PRIMARY KEY (ontologyURI, 
  questionnairePartsID, 
  questionnairePartsTableID));
CREATE TABLE tb_MultiLanguage (
  languageID      int4 NOT NULL, 
  description     varchar(500) NOT NULL, 
  descriptionLang varchar(500) NOT NULL, 
  PRIMARY KEY (languageID, 
  description));
CREATE TABLE tb_Language (
  languageID  SERIAL NOT NULL, 
  description varchar(255) NOT NULL, 
  PRIMARY KEY (languageID));
CREATE TABLE tb_TermType (
  termTypeID  SERIAL NOT NULL, 
  description varchar(255) NOT NULL, 
  PRIMARY KEY (termTypeID));
COMMENT ON COLUMN tb_TermType.description IS 'Description of term type. Example: Class, Object Property, Data Property, Individual';
CREATE TABLE tb_RelationOntology (
  ontologyURI               varchar(255) NOT NULL, 
  questionnairePartsID      int4 NOT NULL, 
  questionnairePartsTableID int4 NOT NULL, 
  predicate                 varchar(255) NOT NULL, 
  relationTypeID            int4 NOT NULL, 
  rangeURI                  varchar(255), 
  rangeDataType             varchar(255), 
  PRIMARY KEY (ontologyURI, 
  questionnairePartsID, 
  questionnairePartsTableID, 
  predicate));
CREATE TABLE tb_RelationType (
  relationTypeID SERIAL NOT NULL, 
  description    varchar(255) NOT NULL, 
  PRIMARY KEY (relationTypeID));
CREATE TABLE tb_User (
  userID              SERIAL NOT NULL, 
  login               varchar(255) NOT NULL UNIQUE, 
  firstName           varchar(100) NOT NULL, 
  lastName            varchar(100) NOT NULL, 
  regionalCouncilCode varchar(255), 
  password            varchar(255) NOT NULL, 
  eMail               varchar(255), 
  foneNumber          varchar(255), 
  PRIMARY KEY (userID));
CREATE TABLE tb_GroupRole (
  groupRoleID SERIAL NOT NULL, 
  description varchar(255) NOT NULL, 
  PRIMARY KEY (groupRoleID));
CREATE TABLE tb_UserRole (
  userID         int4 NOT NULL, 
  groupRoleID    int4 NOT NULL, 
  hospitalUnitID int4 NOT NULL, 
  creationDate   timestamp NOT NULL, 
  expirationDate timestamp, 
  PRIMARY KEY (userID, 
  groupRoleID, 
  hospitalUnitID));
CREATE TABLE tb_NotificationRecord (
  userID         int4 NOT NULL, 
  profileID      int4 NOT NULL, 
  hospitalUnitID int4 NOT NULL, 
  tableName      varchar(255) NOT NULL, 
  rowdID         int4 NOT NULL, 
  changedOn      timestamp NOT NULL, 
  operation      varchar(1) NOT NULL, 
  log            text, 
  PRIMARY KEY (userID, 
  profileID, 
  hospitalUnitID, 
  tableName, 
  rowdID, 
  changedOn, 
  operation));
COMMENT ON COLUMN tb_NotificationRecord.operation IS '(I) Insert
(U) Update
(D) Delete';
CREATE TABLE tb_Permission (
  permissionID SERIAL NOT NULL, 
  description  varchar(255) NOT NULL, 
  PRIMARY KEY (permissionID));
CREATE TABLE tb_GroupRolePermission (
  groupRoleID  int4 NOT NULL, 
  permissionID int4 NOT NULL, 
  PRIMARY KEY (groupRoleID, 
  permissionID));
-- ALTER TABLE tb_AssessmentQuestionnaire ADD CONSTRAINT FKtb_Assessm313417 FOREIGN KEY (participantID) REFERENCES tb_Participant (participantID);
ALTER TABLE tb_AssessmentQuestionnaire ADD CONSTRAINT FKtb_Assessm665217 FOREIGN KEY (hospitalUnitID) REFERENCES tb_HospitalUnit (hospitalUnitID);
ALTER TABLE tb_ListOfValues ADD CONSTRAINT FKtb_ListOfV184108 FOREIGN KEY (listTypeID) REFERENCES tb_ListType (listTypeID);
ALTER TABLE tb_Questions ADD CONSTRAINT FKtb_Questio240796 FOREIGN KEY (listTypeID) REFERENCES tb_ListType (listTypeID);
ALTER TABLE tb_Questions ADD CONSTRAINT FKtb_Questio684913 FOREIGN KEY (questionTypeID) REFERENCES tb_QuestionType (questionTypeID);
ALTER TABLE tb_AssessmentQuestionnaire ADD CONSTRAINT FKtb_Assessm419169 FOREIGN KEY (questionnaireID) REFERENCES tb_Questionnaire (questionnaireID);
ALTER TABLE tb_CRFForms ADD CONSTRAINT FKtb_CRFForm860269 FOREIGN KEY (questionnaireID) REFERENCES tb_Questionnaire (questionnaireID);
ALTER TABLE tb_QuestionGroupFormRecord ADD CONSTRAINT FKtb_Questio928457 FOREIGN KEY (listOfValuesID) REFERENCES tb_ListOfValues (listOfValuesID);
ALTER TABLE tb_Questions ADD CONSTRAINT FKtb_Questio808495 FOREIGN KEY (questionGroupID) REFERENCES tb_QuestionGroup (questionGroupID);
ALTER TABLE tb_QuestionGroupForm ADD CONSTRAINT FKtb_Questio659154 FOREIGN KEY (crfFormsID) REFERENCES tb_CRFForms (crfFormsID);
ALTER TABLE tb_QuestionGroupForm ADD CONSTRAINT FKtb_Questio124287 FOREIGN KEY (questionID) REFERENCES tb_Questions (questionID);
ALTER TABLE tb_Questions ADD CONSTRAINT SubordinateTo FOREIGN KEY (subordinateTo) REFERENCES tb_Questions (questionID);
ALTER TABLE tb_QuestionGroupFormRecord ADD CONSTRAINT FKtb_Questio489549 FOREIGN KEY (crfFormsID, questionID) REFERENCES tb_QuestionGroupForm (crfFormsID, questionID);
ALTER TABLE tb_Questions ADD CONSTRAINT isAbout FOREIGN KEY (isAbout) REFERENCES tb_Questions (questionID);
ALTER TABLE tb_FormRecord ADD CONSTRAINT FKtb_FormRec2192 FOREIGN KEY (crfFormsID) REFERENCES tb_CRFForms (crfFormsID);
-- ALTER TABLE tb_FormRecord ADD CONSTRAINT FKtb_FormRec984256 FOREIGN KEY (participantID, hospitalUnitID, questionnaireID) REFERENCES tb_AssessmentQuestionnaire (participantID, hospitalUnitID, questionnaireID);
ALTER TABLE tb_QuestionGroupFormRecord ADD CONSTRAINT FKtb_Questio935723 FOREIGN KEY (formRecordID) REFERENCES tb_FormRecord (formRecordID);
ALTER TABLE tb_OntologyTerms ADD CONSTRAINT FKtb_Ontolog722236 FOREIGN KEY (ontologyID) REFERENCES tb_Ontology (ontologyID);
ALTER TABLE tb_QuestionnaireParts ADD CONSTRAINT FKtb_Questio42774 FOREIGN KEY (questionnairePartsTableID) REFERENCES tb_QuestionnairePartsTable (questionnairePartsTableID);
ALTER TABLE tb_QuestionnairePartsOntology ADD CONSTRAINT FKtb_Questio144645 FOREIGN KEY (ontologyURI) REFERENCES tb_OntologyTerms (ontologyURI);
ALTER TABLE tb_QuestionnairePartsOntology ADD CONSTRAINT FKtb_Questio773521 FOREIGN KEY (questionnairePartsID, questionnairePartsTableID) REFERENCES tb_QuestionnaireParts (questionnairePartsID, questionnairePartsTableID);
ALTER TABLE tb_MultiLanguage ADD CONSTRAINT FKtb_MultiLa36028 FOREIGN KEY (languageID) REFERENCES tb_Language (languageID);
ALTER TABLE tb_OntologyTerms ADD CONSTRAINT FKtb_Ontolog677035 FOREIGN KEY (termTypeID) REFERENCES tb_TermType (termTypeID);
ALTER TABLE tb_RelationOntology ADD CONSTRAINT FKtb_Relatio952071 FOREIGN KEY (relationTypeID) REFERENCES tb_RelationType (relationTypeID);
ALTER TABLE tb_RelationOntology ADD CONSTRAINT FKtb_Relatio885128 FOREIGN KEY (ontologyURI, questionnairePartsID, questionnairePartsTableID) REFERENCES tb_QuestionnairePartsOntology (ontologyURI, questionnairePartsID, questionnairePartsTableID);
ALTER TABLE tb_RelationOntology ADD CONSTRAINT FKtb_Relatio361398 FOREIGN KEY (predicate) REFERENCES tb_OntologyTerms (ontologyURI);
ALTER TABLE tb_UserRole ADD CONSTRAINT FKtb_UserRol401578 FOREIGN KEY (userID) REFERENCES tb_User (userID);
ALTER TABLE tb_UserRole ADD CONSTRAINT FKtb_UserRol864770 FOREIGN KEY (groupRoleID) REFERENCES tb_GroupRole (groupRoleID);
ALTER TABLE tb_UserRole ADD CONSTRAINT FKtb_UserRol324331 FOREIGN KEY (hospitalUnitID) REFERENCES tb_HospitalUnit (hospitalUnitID);
ALTER TABLE tb_NotificationRecord ADD CONSTRAINT FKtb_Notific397621 FOREIGN KEY (userID, profileID, hospitalUnitID) REFERENCES tb_UserRole (userID, groupRoleID, hospitalUnitID);
ALTER TABLE tb_GroupRolePermission ADD CONSTRAINT FKtb_GroupRo425613 FOREIGN KEY (groupRoleID) REFERENCES tb_GroupRole (groupRoleID);
ALTER TABLE tb_GroupRolePermission ADD CONSTRAINT FKtb_GroupRo893005 FOREIGN KEY (permissionID) REFERENCES tb_Permission (permissionID);


-- Alterações feitas pelo grupo do objetivo 1:
ALTER TABLE tb_questiongroupformrecord ALTER COLUMN answer TYPE varchar(1000);
ALTER TABLE tb_formrecord ADD COLUMN atendimentoID varchar(100) DEFAULT NULL;