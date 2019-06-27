if __name__ == '__main__':
 #####
 ##   Multicrab configuration
 #####
 import sys
 from CRABClient.UserUtilities import config, getUsernameFromSiteDB
 config = config()
 from CRABAPI.RawCommand import crabCommand
 from CRABClient.ClientExceptions import ClientException
 from httplib import HTTPException
 config.General.workArea = 'Crab_projects'

 def submit(config):
  try:
   crabCommand('submit', config = config)
  except HTTPException as hte:
   print "Failed submitting task: %s" % (hte.headers)
  except ClientException as cle:
   print "Failed submitting task: %s" % (cle)
 #####
 ##   Crab configuration
 #####
 datasetnames  = [
'Legacy16V1_SEleBlockB',
'Legacy16V1_SEleBlockC',
'Legacy16V1_SEleBlockD',
'Legacy16V1_SEleBlockE',
'Legacy16V1_SEleBlockF',
'Legacy16V1_SEleBlockG',
'Legacy16V1_SEleBlockH',
'Legacy16V1_SMuBlockB',
'Legacy16V1_SMuBlockC',
'Legacy16V1_SMuBlockD',
'Legacy16V1_SMuBlockE',
'Legacy16V1_SMuBlockF',
'Legacy16V1_SMuBlockG',
'Legacy16V1_SMuBlockH',
'Legacy16V1_DblEGBlockB',
'Legacy16V1_DblEGBlockC',
'Legacy16V1_DblEGBlockD',
'Legacy16V1_DblEGBlockE',
'Legacy16V1_DblEGBlockF',
'Legacy16V1_DblEGBlockG',
'Legacy16V1_DblEGBlockH',
'Legacy16V1_DblMuBlockB',
'Legacy16V1_DblMuBlockC',
'Legacy16V1_DblMuBlockD',
'Legacy16V1_DblMuBlockE',
'Legacy16V1_DblMuBlockF',
'Legacy16V1_DblMuBlockG',
'Legacy16V1_DblMuBlockH',
'Legacy16V1_MuEGBlockB',
'Legacy16V1_MuEGBlockC',
'Legacy16V1_MuEGBlockD',
'Legacy16V1_MuEGBlockE',
'Legacy16V1_MuEGBlockF',
'Legacy16V1_MuEGBlockG',
'Legacy16V1_MuEGBlockH',
                 ]
 datasetinputs = [
 # SingleElectron dataset : AT LEAST 1 high-energy electron in the event.
 '/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD',
 '/SingleElectron/Run2016C-17Jul2018-v1/MINIAOD',
 '/SingleElectron/Run2016D-17Jul2018-v1/MINIAOD',
 '/SingleElectron/Run2016E-17Jul2018-v1/MINIAOD',
 '/SingleElectron/Run2016F-17Jul2018-v1/MINIAOD',
 '/SingleElectron/Run2016G-17Jul2018-v1/MINIAOD',
 '/SingleElectron/Run2016H-17Jul2018-v1/MINIAOD',
 # SingleMuon dataset : AT LEAST 1 high-energy muon in the event.
 '/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD',
 '/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD',
 '/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD',
 '/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD',
 '/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD',
 '/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD',
 '/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD',
 # DoubleEG dataset : AT LEAST 2 high-energy electron in the event.
 '/DoubleEG/Run2016B-17Jul2018_ver2-v1/MINIAOD',
 '/DoubleEG/Run2016C-17Jul2018-v1/MINIAOD',
 '/DoubleEG/Run2016D-17Jul2018-v1/MINIAOD',
 '/DoubleEG/Run2016E-17Jul2018-v1/MINIAOD',
 '/DoubleEG/Run2016F-17Jul2018-v1/MINIAOD',
 '/DoubleEG/Run2016G-17Jul2018-v1/MINIAOD',
 '/DoubleEG/Run2016H-17Jul2018-v1/MINIAOD',
 # DoubleMuon dataset : AT LEAST 2 high-energy muon in the event.
 '/DoubleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD',
 '/DoubleMuon/Run2016C-17Jul2018-v1/MINIAOD',
 '/DoubleMuon/Run2016D-17Jul2018-v1/MINIAOD',
 '/DoubleMuon/Run2016E-17Jul2018-v1/MINIAOD',
 '/DoubleMuon/Run2016F-17Jul2018-v1/MINIAOD',
 '/DoubleMuon/Run2016G-17Jul2018-v1/MINIAOD',
 '/DoubleMuon/Run2016H-17Jul2018-v1/MINIAOD',
 # MuonEG dataset : AT LEAST 1 high-energy electron and 1 high-energy muon in the event.
 '/MuonEG/Run2016B-17Jul2018_ver2-v1/MINIAOD',
 '/MuonEG/Run2016C-17Jul2018-v1/MINIAOD',
 '/MuonEG/Run2016D-17Jul2018-v1/MINIAOD',
 '/MuonEG/Run2016E-17Jul2018-v1/MINIAOD',
 '/MuonEG/Run2016F-17Jul2018-v1/MINIAOD',
 '/MuonEG/Run2016G-17Jul2018-v1/MINIAOD',
 '/MuonEG/Run2016H-17Jul2018-v1/MINIAOD',
                ]

JECBlockBCD = [
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK8PFchs.txt',
]

JECBlockEF = [
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L1FastJet_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L2Relative_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L3Absolute_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L2L3Residual_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_Uncertainty_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L1FastJet_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L2Relative_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L3Absolute_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L2L3Residual_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_Uncertainty_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L1FastJet_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L2Relative_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L3Absolute_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_L2L3Residual_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017EF_V11_DATA/Summer16_07Aug2017EF_V11_DATA_Uncertainty_AK8PFchs.txt',
]

JECBlockGH = [
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L1FastJet_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L2Relative_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L3Absolute_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L2L3Residual_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_Uncertainty_AK4PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L1FastJet_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L2Relative_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L3Absolute_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L2L3Residual_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_Uncertainty_AK4PFPuppi.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L1FastJet_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L2Relative_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L3Absolute_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_L2L3Residual_AK8PFchs.txt',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017GH_V11_DATA/Summer16_07Aug2017GH_V11_DATA_Uncertainty_AK8PFchs.txt',
]


goodRunsLists = [
'/afs/cern.ch/work/b/binghuan/private/TTHLepRunII/CMSSW_10_2_14/src/BSMFramework/BSM3G_TNT_Maker/data/JSON/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt',
]

for d in range(0,len(datasetnames)):
#for d in range(10,len(datasetnames)):
#for d in range(0,10):
#for d in [4,9,14,19,24]:
    print 'multicrab.py: Running datasetname: ', datasetnames[d]
    JECFiles = []
    tempJSON = ''
    if 'BlockB' in datasetnames[d]:
        print 'multicrab.py: Run Block B'
        JECFiles = JECBlockBCD
        tempJSON = goodRunsLists[0]
    if 'BlockC' in datasetnames[d]:
        print 'multicrab.py: Run Block C'
        JECFiles = JECBlockBCD
        tempJSON = goodRunsLists[0]
    if 'BlockD' in datasetnames[d]:
        print 'multicrab.py: Run Block D'
        JECFiles = JECBlockBCD
        tempJSON = goodRunsLists[0]
    if 'BlockE' in datasetnames[d]:
        print 'multicrab.py: Run Block E'
        JECFiles = JECBlockEF
        tempJSON = goodRunsLists[0]
    if 'BlockF' in datasetnames[d]:
        print 'multicrab.py: Run Block F'
        JECFiles = JECBlockEF
        tempJSON = goodRunsLists[0]
    if 'BlockG' in datasetnames[d]:
        print 'multicrab.py: Run Block G'
        JECFiles = JECBlockGH
        tempJSON = goodRunsLists[0]
    if 'BlockH' in datasetnames[d]:
        print 'multicrab.py: Run Block H'
        JECFiles = JECBlockGH
        tempJSON = goodRunsLists[0]

    print 'multicrab.py: JSON File = ', tempJSON
    try:
        testJECFiles = JECFiles[14]
    except(IndexError):
        print 'multicrab.py: Failed to access JEC list element.'
        print 'multicrab.py: Not eneough JEC files proivided.'
        sys.exit()
    try:
        testJSON = goodRunsLists[0]
    except(IndexError):
        print 'multicrab.py: Failed to access JSON list element.'
        print 'multicrab.py: Not eneough JSON files proivided.'
        sys.exit()

    nameJECAK4PFchsDATA1 = "optionJECAK4PFchsDATA1="+JECFiles[0]
    nameJECAK4PFchsDATA2 = "optionJECAK4PFchsDATA2="+JECFiles[1]
    nameJECAK4PFchsDATA3 = "optionJECAK4PFchsDATA3="+JECFiles[2]
    nameJECAK4PFchsDATA4 = "optionJECAK4PFchsDATA4="+JECFiles[3]
    nameJECAK4PFchsDATAUnc = "optionJECAK4PFchsDATAUnc="+JECFiles[4]
    nameJECAK4PFPuppiDATA1 = "optionJECAK4PFPuppiDATA1="+JECFiles[5]
    nameJECAK4PFPuppiDATA2 = "optionJECAK4PFPuppiDATA2="+JECFiles[6]
    nameJECAK4PFPuppiDATA3 = "optionJECAK4PFPuppiDATA3="+JECFiles[7]
    nameJECAK4PFPuppiDATA4 = "optionJECAK4PFPuppiDATA4="+JECFiles[8]
    nameJECAK4PFPuppiDATAUnc = "optionJECAK4PFPuppiDATAUnc="+JECFiles[9]
    nameJECAK8PFchsDATA1 = "optionJECAK8PFchsDATA1="+JECFiles[10]
    nameJECAK8PFchsDATA2 = "optionJECAK8PFchsDATA2="+JECFiles[11]
    nameJECAK8PFchsDATA3 = "optionJECAK8PFchsDATA3="+JECFiles[12]
    nameJECAK8PFchsDATA4 = "optionJECAK8PFchsDATA4="+JECFiles[13]
    nameJECAK8PFchsDATAUnc = "optionJECAK8PFchsDATAUnc="+JECFiles[14]

    config.section_('General')
    config.General.requestName = datasetnames[d]
    config.General.workArea    = datasetnames[d]

    config.section_('JobType')
    config.JobType.pluginName  = 'Analysis'
    # List of parameters to pass to CMSSW parameter-set configuration file:
    config.JobType.psetName    = '/afs/cern.ch/work/b/binghuan/private/TTHLepRunII/CMSSW_10_2_14/src/BSMFramework/BSM3G_TNT_Maker/python/miniAOD_RD2016.py'
    config.JobType.inputFiles = ['/afs/cern.ch/work/b/binghuan/private/TTHLepRunII/CMSSW_10_2_14/src/BSMFramework/BSM3G_TNT_Maker/data/QG/QGL_AK4chs_94X.db']
    config.JobType.allowUndistributedCMSSW = True
    config.JobType.sendExternalFolder = True
    ofParam = 'ofName=' + datasetnames[d]
    config.JobType.pyCfgParams = [nameJECAK4PFchsDATA1,
                                  nameJECAK4PFchsDATA2,
                                  nameJECAK4PFchsDATA3,
                                  nameJECAK4PFchsDATA4,
                                  nameJECAK4PFchsDATAUnc,
                                  nameJECAK4PFPuppiDATA1,
                                  nameJECAK4PFPuppiDATA2,
                                  nameJECAK4PFPuppiDATA3,
                                  nameJECAK4PFPuppiDATA4,
                                  nameJECAK4PFPuppiDATAUnc,
                                  nameJECAK8PFchsDATA1,
                                  nameJECAK8PFchsDATA2,
                                  nameJECAK8PFchsDATA3,
                                  nameJECAK8PFchsDATA4,
                                  nameJECAK8PFchsDATAUnc,
                                  ofParam
                                  ]

    config.section_('Data')
    config.Data.inputDataset   = datasetinputs[d]
    config.Data.inputDBS       = 'global'
    config.Data.splitting      = 'LumiBased'
    config.Data.unitsPerJob    = 30
    # Golden
    config.Data.lumiMask       = tempJSON
    config.Data.outLFNDirBase = '/store/user/binghuan/'
    print 'multicrab.py: outLFNDirBase = /store/user/binghuan/'
    #config.Data.publication = True

    config.section_('Site')
    config.Site.storageSite    = 'T2_CN_Beijing'#'T2_CH_CERN'
    print 'multicrab.py: Submitting Jobs'
    submit(config)
