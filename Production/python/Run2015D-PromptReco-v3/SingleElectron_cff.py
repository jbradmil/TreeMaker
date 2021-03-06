import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/584/00000/DE3323B0-855D-E511-92B0-02163E014187.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/587/00000/7CCA6338-925D-E511-A7FB-02163E0142AF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/629/00000/3E46B406-F35E-E511-8BE2-02163E014318.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/630/00000/6E469C2A-165F-E511-9E77-02163E01414D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/662/00000/1AC0E0A6-025F-E511-B55B-02163E014129.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/672/00000/B258C173-065F-E511-9357-02163E013998.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/673/00000/86A59632-0B5F-E511-8443-02163E014133.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/674/00000/AA2BE3D9-F45E-E511-9D3A-02163E0121D3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/675/00000/864628EB-9C5F-E511-AF26-02163E014767.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/675/00000/D8CD44FA-9C5F-E511-8B24-02163E0134DD.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/675/00000/DC55BAD0-9C5F-E511-84E6-02163E01474C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/675/00000/E24CD8D3-9C5F-E511-A94A-02163E0140FB.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/043AB467-D75F-E511-808D-02163E011DCC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/04B66463-D75F-E511-94D9-02163E01465C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/182CE8AF-D75F-E511-81FE-02163E01441B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/1EBCC17B-D85F-E511-A795-02163E0140F7.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/200CB644-D85F-E511-93EA-02163E014538.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/20360E6E-D75F-E511-82E7-02163E013450.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/209D7E6E-D75F-E511-9593-02163E013450.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/2601EE67-D75F-E511-BD0F-02163E0126EC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/4A424EE3-D75F-E511-A901-02163E0145B9.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/58924A6B-D75F-E511-937D-02163E011C89.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/74BC7275-D75F-E511-A7BA-02163E0146A6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/764F21D7-D75F-E511-8AED-02163E014553.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/88021A74-D75F-E511-AA9D-02163E01465C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/8EBDFB7B-D75F-E511-9318-02163E0146C3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/9673636F-D75F-E511-B414-02163E0145C4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/96DE2B9B-D75F-E511-BA2D-02163E01453C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/AE28EE67-D75F-E511-9191-02163E0126EC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/B6EE076C-D75F-E511-AD8E-02163E0145EF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/BA5DDB70-D75F-E511-80C8-02163E01349E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/BC36876C-D75F-E511-8FC4-02163E0145EF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/E255B585-D75F-E511-9255-02163E012AAD.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/E281063F-D85F-E511-8352-02163E0142DA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/676/00000/F06B278B-D75F-E511-A305-02163E0142AA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/04A8EBBF-345F-E511-A729-02163E01435B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/1AA77AC6-345F-E511-8175-02163E0126BC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/705E47C4-345F-E511-BD2B-02163E014638.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/70E49EC8-345F-E511-B885-02163E01350A.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/74E4B9BD-345F-E511-BE50-02163E01246B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/B65B04BA-345F-E511-9DB2-02163E01346A.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/CAE5CFD7-345F-E511-87C0-02163E01363C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/CECD47C4-345F-E511-BA52-02163E014638.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/677/00000/E41946C8-345F-E511-B2C0-02163E014335.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/721/00000/90A650B7-075F-E511-BE5E-02163E013714.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/725/00000/A0FD11F3-2A5F-E511-8DAF-02163E0133F2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/727/00000/DA7BC76C-395F-E511-A67F-02163E011C56.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/728/00000/08827929-415F-E511-9D34-02163E014722.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/00179335-7460-E511-8EE6-02163E0139BC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/06DA6564-7760-E511-9E26-02163E014421.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/082E7474-6C60-E511-A4E3-02163E013566.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/08663685-7560-E511-9A92-02163E01463F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/14722E35-7460-E511-9802-02163E012096.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/2463D28B-6E60-E511-B7FA-02163E01427D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/2A9EFFF6-A360-E511-83F1-02163E013759.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/32AC4D36-7460-E511-993D-02163E0137F5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/403A25AA-6E60-E511-9687-02163E0124F4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/4415FD67-7760-E511-B802-02163E011E08.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/54D573D9-7860-E511-B4C1-02163E011C91.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/5AA35F52-7260-E511-B56F-02163E01469A.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/5C287754-7260-E511-8327-02163E014640.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/5E29296D-7260-E511-8EC7-02163E0145F6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/60AF0A39-7460-E511-89A3-02163E0144EA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/60F5DB35-7460-E511-AC79-02163E011D99.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/728240EF-7060-E511-8685-02163E0133E9.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/72A4046D-6C60-E511-81A4-02163E0137CA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/760FB377-6C60-E511-B1D2-02163E014718.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/7E3C579C-6E60-E511-8D94-02163E014229.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/8AEF5285-7560-E511-B15E-02163E011E10.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/900D3A3F-7460-E511-8214-02163E014230.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/90D9F435-7460-E511-B389-02163E011E08.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/96E81D79-7560-E511-A30A-02163E0143CD.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/9AD6F795-6E60-E511-85AC-02163E0145DA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/A8F3FE65-6C60-E511-BA88-02163E012096.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/AC342153-7260-E511-A9DB-02163E014318.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/ACCC7D59-7260-E511-8679-02163E0124F4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/B241EB76-6C60-E511-8462-02163E0139BC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/B2D7FCD9-7060-E511-9BC0-02163E012096.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/B86834A9-6E60-E511-97B4-02163E01370D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/BC55EC67-6660-E511-BBF1-02163E01463F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/CAA1046D-6C60-E511-AC5D-02163E0137CA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/EEA58A8C-6C60-E511-AC7F-02163E0145F6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/FAAE8954-7260-E511-BD80-02163E0143CD.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/729/00000/FAF0205D-7260-E511-A471-02163E0144F5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/734/00000/5212737C-0060-E511-8750-02163E0145ED.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/734/00000/86A9F056-0060-E511-9F37-02163E013487.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/734/00000/A4DEB277-0160-E511-A1EA-02163E01419D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/734/00000/BC8F6458-0060-E511-A1DF-02163E01364B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/798/00000/0C7A577A-B15F-E511-8AE8-02163E011BBE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/801/00000/02D58F8E-5460-E511-ACE4-02163E01470E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/801/00000/10629A2B-5360-E511-9715-02163E014353.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/801/00000/1217EA24-5360-E511-A5D8-02163E014750.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/801/00000/C6BC5316-5360-E511-AFE0-02163E0144EA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/801/00000/E2F1C53E-5360-E511-B07D-02163E0140EC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/834/00000/BCB77EEA-FE5F-E511-AD5D-02163E0136FE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/842/00000/5C1E8939-4460-E511-BFE6-02163E014534.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/0C1B4D82-7561-E511-80DA-02163E0142D5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/0EC80E85-7561-E511-BB6A-02163E0145D2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/204DDA6D-7561-E511-95EF-02163E012B24.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/20C82C64-7561-E511-9A8B-02163E0139C3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/32D5DA69-7561-E511-B902-02163E0146F5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/32DC296E-7561-E511-A2E8-02163E011DD4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/506B7183-7561-E511-B686-02163E011906.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/58EDE17E-7561-E511-9D5E-02163E01392D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/5CEA4970-7561-E511-8B9C-02163E011AC2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/6AE0616D-7561-E511-9C25-02163E012861.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/7A980471-7561-E511-93E1-02163E01443B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/7C6BE01E-7661-E511-9743-02163E0138BA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/88108D6C-7561-E511-B3E9-02163E014412.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/90927775-7561-E511-97F4-02163E01442F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/92207281-7561-E511-9E49-02163E012B18.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/941E9379-7561-E511-98EE-02163E013393.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/980A9D70-7561-E511-BCB7-02163E012B1C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/9E2AFA60-7561-E511-A618-02163E0146F5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/AE1F4A70-7561-E511-801F-02163E011AC2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/B8755465-7561-E511-B65A-02163E0142FF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/C07DDC7C-7561-E511-8F20-02163E012B2E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/C2E2CA81-7561-E511-B45C-02163E011C7D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/DE6F8D70-7561-E511-81D8-02163E014660.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/E4320085-7561-E511-ACC0-02163E0133F8.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/E820C271-7561-E511-B998-02163E011838.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/843/00000/FC913097-7561-E511-8B85-02163E0138D9.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/865/00000/CE2DE2F5-ED60-E511-9643-02163E014552.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/866/00000/84B4359E-F660-E511-B47B-02163E011D9F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/867/00000/4C0A288E-1961-E511-8B3D-02163E0141AB.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/867/00000/5425B5A1-1961-E511-924D-02163E013582.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/867/00000/ECAE9A90-1961-E511-AC82-02163E011A29.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/0C3D6566-9361-E511-8377-02163E0137F3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/1C2AEC73-9361-E511-8942-02163E014610.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/1ED7C757-9361-E511-A10A-02163E012B11.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/50648A5D-9361-E511-8B5E-02163E013520.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/5AAE9760-9361-E511-82FF-02163E014249.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/B2FB4058-9361-E511-B06E-02163E0138C1.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/D0984B6A-9361-E511-91D8-02163E013576.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/DE30B659-9361-E511-B25B-02163E01443C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/E28F8B53-9361-E511-94F7-02163E014752.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/E4A88E58-9361-E511-B29D-02163E0144C4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/F04A318F-9361-E511-8A82-02163E01181F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/868/00000/FE48CC5B-9361-E511-AD65-02163E0138C1.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/869/00000/0C5CE49F-1B61-E511-9E64-02163E013557.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/924/00000/D8BF0832-6261-E511-989A-02163E013411.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/925/00000/16428679-6461-E511-84B1-02163E0126F2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/926/00000/825C4A4C-4667-E511-A0B1-02163E0126E8.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/935/00000/7E85FC02-A061-E511-A7F2-02163E01469A.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/0488E437-3662-E511-A17B-02163E011DD4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/10D09C3A-3662-E511-AD85-02163E01284C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/1227B23A-3662-E511-B11E-02163E0142FA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/144AA437-3662-E511-9202-02163E014145.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/20F1734B-3662-E511-A7EB-02163E0141D6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/4AED9143-3662-E511-84C1-02163E0141BE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/6AB07E32-3662-E511-942D-02163E0140DB.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/9CC5BB35-3662-E511-ACD4-02163E0145A3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/BC0AA73A-3662-E511-83AB-02163E01369C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/C86DA838-3662-E511-99F0-02163E011B9C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/CA725F39-3662-E511-BFC7-02163E0141DE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/DA0ADF39-3662-E511-B4F5-02163E0135C3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/E2AF8946-3662-E511-AB1F-02163E011F95.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/EC337E37-3662-E511-AC0B-02163E011F18.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/FCA4783E-3662-E511-A401-02163E01387D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/936/00000/FE813A3E-3662-E511-94F5-02163E014605.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/941/00000/008F855B-1962-E511-A3AC-02163E012A7D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/941/00000/00EBA83B-1962-E511-8A55-02163E014362.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/941/00000/1C84506B-1962-E511-9441-02163E014113.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/941/00000/1CCC9141-1962-E511-8962-02163E0127E5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/941/00000/9E46FD4C-1962-E511-9D91-02163E0127E5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/256/941/00000/EAC0BB45-1962-E511-A45C-02163E011F3B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/024/00000/C08349A4-2562-E511-93EC-02163E014668.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/027/00000/7AD4FCDA-3062-E511-82D1-02163E01470F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/394/00000/5EBDE45C-4364-E511-87FD-02163E0146A6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/395/00000/22B7FD01-1D64-E511-BAAD-02163E014585.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/396/00000/BE12E5BA-1565-E511-A5F7-02163E0141CE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/397/00000/00BC787E-5664-E511-8892-02163E0124DF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/397/00000/1641237F-5664-E511-B6E7-02163E014113.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/397/00000/928FC166-5664-E511-A25B-02163E01434D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/397/00000/D079A767-5664-E511-BAA5-02163E0145FE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/398/00000/BE04FFC5-3B64-E511-A31A-02163E01475E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/30493B01-5964-E511-9A80-02163E0133EA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/70D02E46-5964-E511-AA29-02163E014113.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/844B450A-5964-E511-B244-02163E0144AC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/84D10302-5964-E511-B35D-02163E0139A6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/88D1F439-5964-E511-B8BB-02163E01434D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/BE8827F2-5864-E511-B5F0-02163E0142FF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/399/00000/F0AAFC04-5964-E511-90EE-02163E011F37.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/08EB9D50-5465-E511-9569-02163E011DE0.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/10C1C487-5465-E511-93D8-02163E0138E3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/148EA067-5465-E511-8BAE-02163E012239.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/1E30817B-5465-E511-B534-02163E01436F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/22B6FDB4-4B65-E511-8815-02163E01436F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/2405E889-5465-E511-A5B7-02163E0143FA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/2C989B63-5465-E511-86F9-02163E0134FC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/32A286B8-5465-E511-A8E7-02163E01436F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/36E9216E-5465-E511-86FA-02163E0142ED.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/40DC729D-5465-E511-9AD4-02163E01465E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/424BD65A-5465-E511-9B8C-02163E0138E3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/4459436F-5465-E511-B046-02163E011812.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/50BB716E-5465-E511-AC7F-02163E014728.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/68B7D762-5465-E511-AE0E-02163E0144FA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/6C98825A-5465-E511-A44D-02163E0138E6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/8088AF5B-5465-E511-8A8B-02163E013458.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/82788E67-5465-E511-A857-02163E0142D2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/86666AB2-5465-E511-89C7-02163E0142F4.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/8A013067-5465-E511-BE36-02163E013904.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/8CDB0573-5065-E511-A893-02163E011C24.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/8E642B69-5465-E511-8090-02163E0138E6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/A8DCC35C-5465-E511-97F2-02163E013458.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/BCDC985F-5465-E511-83D1-02163E013886.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/CA588B44-5265-E511-8C2D-02163E01448E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/DCC90E7C-5065-E511-8668-02163E013645.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/EA078FCC-5165-E511-88F0-02163E014456.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/EC71F952-5465-E511-B5C4-02163E011802.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/400/00000/F65B3F50-5465-E511-BF76-02163E0142FF.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/460/00000/AE49B616-DB64-E511-B4BA-02163E0144B7.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/461/00000/2E26CDFB-7265-E511-9D1A-02163E01433E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/461/00000/76EC8AF8-7265-E511-A031-02163E01204B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/16DD6163-4F66-E511-BB33-02163E0134E3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/20A4F3CD-4A66-E511-977C-02163E0138E0.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/24866D83-4966-E511-B302-02163E0145E2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/324354C6-4A66-E511-B7C3-02163E012BA0.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/56E98099-4966-E511-A099-02163E011F09.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/5AC85771-4966-E511-9397-02163E011F59.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/7640B7BD-4A66-E511-A410-02163E014186.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/9E04C5EA-4666-E511-804D-02163E0133F0.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/9E380277-4966-E511-8A01-02163E014433.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/DA393CE4-4666-E511-9BDF-02163E013660.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/487/00000/EACEC6F6-3B66-E511-8374-02163E011DE0.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/490/00000/0CFC753F-4566-E511-BA23-02163E0133F1.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/490/00000/BA22E1DF-5066-E511-BEBB-02163E0119A6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/529/00000/787D4467-C665-E511-A354-02163E0146D3.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/531/00000/024E80E0-1F66-E511-9B68-02163E0142FE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/531/00000/1ABF51E0-1F66-E511-972E-02163E0124DC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/531/00000/50A6B405-2066-E511-94A6-02163E012754.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/531/00000/68358FE3-1F66-E511-90E4-02163E01446D.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/531/00000/EC762CE0-1F66-E511-8517-02163E014334.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/598/00000/4AAAA27D-2A66-E511-A0A8-02163E0146F9.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/599/00000/044ED018-6366-E511-8159-02163E0133A2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/599/00000/168E6806-6366-E511-B58A-02163E01198F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/599/00000/ECCC19D2-6266-E511-8D92-02163E011FA2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/611/00000/A4265F7F-6366-E511-B6C9-02163E014405.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/08DAFFBD-4367-E511-835E-02163E013590.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/12AA99B8-4367-E511-A5B7-02163E012095.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/18AFE5AC-4367-E511-BBA3-02163E0134AB.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/1AE830BD-4367-E511-A16A-02163E0143AC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/2275BABC-4367-E511-A48F-02163E014410.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/2A471BB9-4367-E511-B1B6-02163E0133C6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/345819B9-4367-E511-A30B-02163E01364A.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/36D38BBF-4367-E511-A47D-02163E014552.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/3CB89EBC-4367-E511-907A-02163E01193F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/4259FBBD-4367-E511-A4AD-02163E011F0B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/441E79BA-4367-E511-84E3-02163E0136EC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/4452F1D6-4367-E511-AA58-02163E01453F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/4A3B23BB-4367-E511-9384-02163E01371E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/4E9A6AC5-4367-E511-B67A-02163E011979.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/50FDA4BC-4367-E511-946C-02163E0118A6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/520D1FC2-4367-E511-8428-02163E011FC7.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/52A62EBF-4367-E511-A182-02163E0146ED.root' ] );
readFiles.extend( [

       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/56464ABE-4367-E511-9815-02163E01414A.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/5EAADDCD-4367-E511-BADA-02163E0146EA.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/609963C0-4367-E511-9904-02163E01349B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/6492AAC2-4367-E511-9D9A-02163E0142D2.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/6CC916B8-4367-E511-A36D-02163E011A9F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/80A8EAB9-4367-E511-ADE7-02163E01390E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/8454E9C4-4367-E511-9946-02163E011B54.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/88164BBB-4367-E511-AD01-02163E013976.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/88946BC2-4367-E511-AF23-02163E0145DC.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/9C210BC3-4367-E511-9E48-02163E0136D9.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/9C496DC5-4367-E511-8863-02163E0119F6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/AEA8A3B9-4367-E511-BD72-02163E014598.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/BA573EC3-4367-E511-B91F-02163E01338E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/C252E1B8-4367-E511-AD75-02163E01475E.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/D01616BC-4367-E511-899D-02163E01342B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/D07339B9-4367-E511-BA1F-02163E01462F.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/D20631F0-4367-E511-A7C1-02163E0140E5.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/D2E822B8-4367-E511-8C3E-02163E013756.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/D47D70BA-4367-E511-9AFC-02163E01437B.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/EE37D8BA-4367-E511-8E9F-02163E0140FE.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/EE9B16C8-4367-E511-A7A4-02163E0138E6.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/613/00000/F2EA8FE2-4367-E511-BDC6-02163E01464C.root',
       '/store/data/Run2015D/SingleElectron/MINIAOD/PromptReco-v3/000/257/644/00000/8A88F7ED-1867-E511-B40A-02163E011B2F.root' ] );


secFiles.extend( [
               ] )

