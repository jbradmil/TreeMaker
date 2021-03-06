import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/026BD647-591F-E611-9469-B083FED3F2E9.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/127238C0-F81F-E611-93DC-0CC47A4D7692.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/189C2D83-4D1F-E611-A74C-842B2B1732D5.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/1AC41C0D-551F-E611-99C8-0025905B8568.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/2C610703-3E1F-E611-83DA-549F3525DFE8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/321E69A6-5C1F-E611-B277-0CC47A4D7636.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/360AE97C-4D1F-E611-95D6-1418773425EA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/48A1AC01-3E1F-E611-A3E5-B083FED04D68.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/5AB30851-781F-E611-ABAD-0CC47A4D76B2.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/668867A5-5C1F-E611-B70A-0CC47A78A426.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/6E94AEEC-321F-E611-A21D-003048FF9ABC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/720DDAD5-2D1F-E611-AFDB-14187741278B.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/76B6D369-4D1F-E611-A2E4-782BCB2100C5.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/7CD0464E-621F-E611-970E-B083FED3EE25.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/96E71C54-781F-E611-9AC2-0025905A48BC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/9E2D9246-591F-E611-9CBA-B083FECFF52E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/B219B953-5C1F-E611-9B7F-0CC47A78A3E8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/B2C82A6C-F01F-E611-9134-782BCB1EBB34.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/BCA3AA69-4D1F-E611-A43C-141877411936.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/C25B6CD2-2D1F-E611-81BC-842B2B17EA37.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/C2BAE75F-4D1F-E611-A6EC-B083FED42ED0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/C41D7DE4-871F-E611-937C-0CC47A4C8E16.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/CA5B01EB-541F-E611-9FB1-0025905A608E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/CED61DEB-541F-E611-B46C-003048FFD7CE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/D6886168-4D1F-E611-84FC-842B2B1812E7.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/E25B549F-D01F-E611-8930-0025905A609E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/F08AB338-551F-E611-B1B8-0CC47A4C8E70.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/F62B917A-4D1F-E611-80F4-1418774124DE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/F80D4C6D-4D1F-E611-A00A-141877411970.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/00000/FA1F530E-551F-E611-8666-0025905B861C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/00F24225-EC21-E611-AAD3-0CC47A78A418.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/10E72227-EC21-E611-8FDA-0CC47A78A4B8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/1223F728-EC21-E611-818A-0025905A6088.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/1628478C-B721-E611-8FDB-0CC47A7452D0.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/180A8993-A321-E611-9ABE-0025905B85FC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/42C27EA4-E122-E611-8832-0025905B85F6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/4EBC9693-A321-E611-A4BF-782BCB20E307.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/526E7022-B721-E611-80BF-0CC47A78A458.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/6251EE2B-EC21-E611-A5BB-0025905A607E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/6E0EFFD1-A321-E611-BF1F-A4BADB1E6F7A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/709A5163-E022-E611-B246-0CC47A6C0716.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/72A69859-E022-E611-AE9A-44A84224BE51.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/848AFF28-EC21-E611-B0FC-0025905B85CA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/887203D2-A222-E611-A757-0CC47A4C8E82.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/8C145111-B721-E611-9495-0CC47A4D763C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/AA58A4EC-A222-E611-B1D8-0025905B856C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/C21C7793-A321-E611-8790-0025905A6066.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/C8F871B1-A321-E611-8C66-782BCB206470.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/CC3F92A5-B721-E611-954A-0CC47A78A340.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/D4AA969C-A321-E611-9356-549F3525AE58.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/E4E3070B-B721-E611-B529-0025905A60C6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/2065C700-CD20-E611-BDC1-0CC47A4D766C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/3C0A7621-CE20-E611-86B6-549F3525B220.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/46401C51-EF20-E611-82AE-14187741121F.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/664100E6-AA20-E611-A048-0CC47A74525A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/6E15DADA-AA20-E611-B24D-0025905A60AA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/7CEE46EC-B221-E611-B553-008CFA197DA4.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/86AE22BE-A520-E611-AD89-A4BADB1CF89C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/98C3104B-EF20-E611-98AE-0CC47A4D760A.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/A0652D28-9121-E611-8C0E-0025905B85D6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/B2AD6A65-EF20-E611-BDAD-0025905B85B2.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/BA6400D8-AA20-E611-A92F-0CC47A4D7634.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/C4B83B97-B620-E611-BCAA-D4AE527EE0EB.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/CAB23DC4-A520-E611-8AAE-90B11C0BD360.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/CED67169-B221-E611-9E60-549F3525BBCC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/D0B5BBF5-AB20-E611-9A69-0CC47A4D768E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/D85547D7-AA20-E611-AC92-0CC47A4C8F08.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/E4368705-CD20-E611-A617-0CC47A4C8E82.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/E8042866-B221-E611-B26A-0CC47A745298.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/EE8EDA45-7C21-E611-A441-0CC47A78A2EC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/FA488CA3-B620-E611-84E8-A4BADB1E6B36.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/60000/FAF9F081-B221-E611-84C1-0025905B85D8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/0453DF14-581F-E611-870D-0025905A6110.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/0CD90AE0-DC1F-E611-8F89-0025905B857E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/14140435-381F-E611-9509-A4BADB1C0EF3.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/266CA91E-581F-E611-9E56-0CC47A4D768C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/288E84E8-3820-E611-96EE-0CC47A78A2F6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/34E7DF38-381F-E611-AFE2-0CC47A78A418.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/3E09DED7-551F-E611-A8E4-0026B93AA8FF.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/4EC29032-5B20-E611-9508-0025905B85D6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/5CF5D622-581F-E611-9B0B-003048FFD79E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/6086A184-2D1F-E611-B062-782BCB20F910.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/62076A36-581F-E611-94A0-0025905B858C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/62428803-911F-E611-A126-0CC47A4C8EBA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/648B2443-2D20-E611-B165-0026B93A2144.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/6A80F222-581F-E611-835D-003048FFD72C.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/74238D35-581F-E611-8DDF-0025905A60B8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/742FBB34-381F-E611-8BA5-0CC47A4C8E14.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/76FE6237-581F-E611-87F8-0025905A6094.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/88C432E2-DC1F-E611-A1F8-0025905B8564.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/8A770A01-911F-E611-845C-0CC47A4D75F8.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/8C63DA3A-581F-E611-9958-0025905B8586.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/8C6FB5D3-551F-E611-854D-A4BADB1C5E28.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/90481E3B-581F-E611-B85F-0025905A609E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/9A1D503F-391F-E611-9DD5-782BCB1F0EBA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/B2948911-581F-E611-9EBE-0CC47A4D769E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/BC27AE47-381F-E611-ADE5-D4AE526DDB41.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/BED9D31B-581F-E611-9D56-0CC47A78A30E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/C0736A16-581F-E611-BD20-0025905B85AA.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/C44492D0-551F-E611-8F17-B083FED024B2.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/C499E313-581F-E611-8611-0CC47A4C8ECE.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/E0B22C42-381F-E611-8A46-782BCB517BF6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/70000/E6F4BFE7-3820-E611-BDFB-0CC47A4D761A.root',
] )
