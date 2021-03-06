import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/004E2E5E-B0FB-E511-9DAD-A4BADB1E74F9.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/066BA6AB-40FB-E511-803B-008CFA1974A0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/10A65624-BFFA-E511-A946-B083FED3EE25.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/147C46C7-CAFA-E511-90BC-549F3525D084.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/16C8F1CC-B2FA-E511-9490-008CFAF207AC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/1EB6D0C1-B0FB-E511-BEB2-008CFA111280.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/20F9BFB1-BAFA-E511-AC01-008CFA197DB8.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/285D33A6-B4FA-E511-841A-0002C94CD1E0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/2C8FEFFA-E0FA-E511-A6BC-0025902BD8CE.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/38BCA8A3-B4FA-E511-98BA-A0369F3102B6.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/4260C817-BEFA-E511-B28A-000F530E4AB0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/4E9F12A5-40FB-E511-874C-008CFA110C78.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/5C2D2B14-E1FA-E511-8DD5-0025907D250C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/5E118524-F0FA-E511-BCDE-002590D9DA9C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/6A197836-C8FA-E511-B3FB-008CFA111210.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/70DC586F-C2FA-E511-8F21-008CFA197AB0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/7C0F4969-A7FB-E511-85C1-0CC47A4C8EC6.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/7CD033D4-D7FA-E511-B869-008CFA1111AC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/8432D735-40FB-E511-AF33-0CC47A0AD456.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/8471A788-B0FB-E511-B14B-90B11C282313.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/8C3612DA-BEFA-E511-9C7B-141877411FED.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/8C6756F6-AFFA-E511-8739-782BCB284437.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/94BFFE38-B0FA-E511-926E-008CFAF06A32.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/94ECD9C7-D2FA-E511-BF6B-002590D9D8AA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/9803D80B-02FB-E511-AD03-008CFA197418.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/98701DB1-E1FA-E511-B0A7-002590D9DA9C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/B2FB8936-C8FA-E511-8A08-008CFA197E18.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/B63EA65C-8EFB-E511-A7DE-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/BE5C4E37-C8FA-E511-BCE5-008CFA16615C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/C66752D5-F9FA-E511-8C28-002590D9D84A.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/CA7FA90B-BFFA-E511-A9AB-90B11C08CA45.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/CC2895FA-CAFA-E511-A5ED-782BCB20DE6B.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/CCB80934-BFFA-E511-8D11-008CFA1974A0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/CE8BEC19-D1FA-E511-B5EE-001E675A4759.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/D034EA70-C2FA-E511-A70B-008CFA1113E8.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/D26FD93E-C8FA-E511-8146-008CFA16615C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/D87B620C-ECFA-E511-9D19-0CC47A57D13E.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/DAC08A08-BDFA-E511-A479-24BE05CE1E31.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/E24BDF00-D8FA-E511-BB3E-008CFA11123C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/E4112AB1-BAFA-E511-AFC4-008CFA197E90.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/E42EDAC1-40FB-E511-A61E-008CFA111280.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/E8AF996B-A7FB-E511-AD80-001E67DDC4AC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/E8C2292F-BFFA-E511-868D-0025904B6FF6.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/EA41316C-C2FA-E511-94E8-000F530E4790.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/EE864734-C8FA-E511-B4C7-008CFAF06480.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/EECDB5CC-B0FB-E511-B1CC-842B2B185470.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/F488E919-88FB-E511-A590-0025904A93AA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/20000/F8A31D14-BEFA-E511-8FA9-90B11C050395.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/02535196-2BFB-E511-9153-008CFA197454.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/02967AB7-11FB-E511-BB4D-24BE05CEFDF1.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/02C16224-28FB-E511-80CB-008CFA1974BC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/02D21E88-24FB-E511-8E12-000F532734A4.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/06411634-1DFB-E511-824C-008CFA197BD4.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/0642F1EF-07FB-E511-8A3D-782BCB408696.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/0CE7E415-7AFB-E511-A726-008CFA1113FC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/0EED28C1-1EFB-E511-A6DE-0025902BD8CE.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/14DC30D6-07FB-E511-8DDC-B083FED76D99.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/1839A121-FAFA-E511-B668-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/2EB910AB-D3FB-E511-A57E-1C6A7A266C63.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/32F167D8-C8FA-E511-979C-008CFA197480.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/36A9B27B-12FD-E511-B630-14187741278B.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/389F8F97-32FB-E511-B3E5-008CFA197964.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/3C2A2E6D-D5FA-E511-811C-A0369F3102B6.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/485E2B1A-86FB-E511-BB5F-008CFA197DB8.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/50F5FB9F-D7FA-E511-AEDC-24BE05C63791.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/524A7F64-F6FB-E511-9137-0CC47A78A2EC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/6634D322-12FD-E511-B660-90E2BA726B80.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/6E33C98F-CDFA-E511-ADD3-008CFA111270.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/6EE181FF-1EFB-E511-B4C3-0002C94CD0BC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/705EC313-FAFA-E511-A250-5065F3818291.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/7AB0B85D-04FB-E511-8F56-001517FA7A98.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/84A2C68B-BDFA-E511-BAB9-008CFA111320.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/8663F09D-5DFC-E511-A1E7-0CC47A0AD456.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/906280B1-02FB-E511-893D-001517E74088.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/9ADE598D-BDFA-E511-8B14-008CFA111280.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/9E1DD6DA-12FD-E511-82A9-008CFA1111F4.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/A2757976-4CFB-E511-9619-90B11C2CB7A9.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/A2EE25DA-C8FA-E511-9F8B-008CFA197990.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/B2BE0B94-02FB-E511-A0BF-90B11C06954E.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/B879377D-31FB-E511-BFDD-008CFA197964.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/BA506594-CDFA-E511-BF8C-008CFA197D9C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/BAFD47FB-1CFB-E511-B5B0-008CFA14F970.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/BC276617-25FB-E511-B4E7-008CFA1111D0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/BE6C0195-24FB-E511-9738-008CFA110D5C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/CE14CE1F-28FC-E511-90F6-B083FED43141.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/D4BAD102-32FB-E511-A741-008CFA1111AC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/D8106549-6CFB-E511-ACC0-0CC47A6B5B20.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/DA7C5C6E-CEFA-E511-9A60-C81F66B73923.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/DE1D5A19-EFFA-E511-8E03-001517E741C8.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/E608296C-D5FA-E511-A887-A0369F3016EC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/E826CE32-26FB-E511-BE8A-782BCB1F0EBA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/EA68F89F-D7FA-E511-9F37-24BE05C63651.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/EE3FDF14-28FB-E511-AA36-008CFA197CCC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/F06E4517-0BFC-E511-B8C4-000F530E46D0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/F2253F8A-D2FA-E511-B9AA-24BE05BDAE61.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/F69A10CE-D4FB-E511-85C5-001E67A3FD26.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/F80538B5-3BFB-E511-B5F3-0025907E35AA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/FAFC2844-F4FB-E511-B7CB-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/0253CE5F-A8FB-E511-AB11-008CFA197964.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/14FE7EF8-5BFB-E511-8FF6-002590550538.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/229036D5-59FB-E511-8927-008CFA197900.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/3AA65E48-5EFB-E511-A422-008CFA197954.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/3CC4638C-5EFB-E511-BA51-008CFA111314.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/40063D90-31FB-E511-9A9B-141877411D77.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/44EB7970-5DFB-E511-B10B-14187741278B.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/4A0A7C06-5FFB-E511-B111-00259055C83A.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/4E97BD75-5EFB-E511-A15B-14187741278B.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/523489E1-5DFB-E511-8115-C81F66B7ED99.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/5E084B08-31FB-E511-87F6-008CFA1661B4.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/62AB3846-5EFB-E511-8A73-0026B93B1193.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/62AECACF-71FB-E511-B4A6-002590550538.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/6A90E10E-5FFB-E511-A727-0025905505FC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/6AD36197-31FB-E511-8806-842B2B172901.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/6E46B194-31FB-E511-B5F2-B083FED3F2E9.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/8054C081-5BFB-E511-861B-0025905487EC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/86836298-31FB-E511-95C5-B083FECFEF7D.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/9803F0FA-5EFB-E511-B47A-00259055C8D6.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/BC27248F-5DFB-E511-AF42-1418774126FB.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/C67DB80A-5CFB-E511-A00B-008CFA11123C.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/C801C02D-C4FB-E511-B856-549F3525D084.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/CE5C8608-31FB-E511-8B70-008CFA197454.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/D2FF7ED2-71FB-E511-A564-008CFA197D18.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/DA14E912-5FFB-E511-8C6E-0025905487EC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/DEAC1DE9-71FB-E511-AA4C-008CFA166188.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/E8F2F2AA-5DFB-E511-972C-B083FED024B2.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/EAEC9DB7-72FB-E511-8934-782BCB206470.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/EC0034E9-71FB-E511-B9D0-008CFA166188.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/50000/FA651E7A-5BFB-E511-945C-008CFA197900.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/08C748BD-0AFC-E511-A29B-90B11C08C1BA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/0CA50D97-DBFA-E511-A1FA-90B11C0BCE74.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/1AD21D14-AFFA-E511-A3D7-0002C94D5504.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/248FC36E-FFFB-E511-8B92-D4AE527EE013.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/2870C938-FBFA-E511-95DD-008CFA197A20.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/340D770C-0DFB-E511-B198-008CFA197CD0.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/3887D8F1-E2FB-E511-8484-A0000420FE80.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/3EB6BAC2-73FB-E511-B43A-0025905B85B8.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/40E4206E-55FB-E511-B4AF-002590D9D8B4.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/46FCE972-1EFB-E511-A1DE-B083FED42B3B.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/4AF80868-D3FA-E511-91B0-782BCB50ACF1.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/50286E55-E1FA-E511-A32F-002590D9D92A.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/54EC8E2A-FBFA-E511-A1F9-0CC47A57CC26.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/5C625438-E1FA-E511-8106-0CC47A57CB62.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/667C962D-C2FA-E511-86B3-001E675A6C2A.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/72BF5F68-7DFB-E511-93C9-0CC47A4D7674.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/8E3BF84B-FBFA-E511-A1F6-008CFA197B74.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/8EAD6A00-0DFB-E511-9E9D-008CFA1974CC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/9445CC0F-C2FA-E511-B485-90B11C08C1BA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/9812C69E-DBFA-E511-A7BE-842B2B173478.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/ACC794BE-C4FA-E511-8971-782BCB20FDEA.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/C09F9F85-65FB-E511-A72F-008CFA1C93FC.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/C662E72B-AFFA-E511-9FF4-0002C94CD0B8.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/F0320EB9-C4FA-E511-977C-0026B939DCF3.root',
       '/store/mc/RunIISpring16MiniAODv1/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/80000/F6F95795-D6FA-E511-9DCE-001E67A3EC05.root',
] )
