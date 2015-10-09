
'''

Ntuple branch template sets for topological variables (MT, etc)

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

mtToMET = PSet(
    # Raw means no MET corrections
    objectMtToMET = 'mtMET({object_idx}, "raw")',

    #PF Type1 MET (and systematics)
    objectMtToPFMET      = 'mtMET({object_idx}, "", "pfmet", ""     , 1)',#1, apply phi correction; all PFMET is type1 in miniAOD ...
    objectMtToPfMet_Ty1  = 'mtMET({object_idx}, "", "pfmet", "type1", 1)',#    but scale uncertainties (jes,ues, etc.) may still be applied
    objectMtToPfMet_mes  = 'mtMET({object_idx}, "", "pfmet", "mes+" , 1)',#    Phi corrections not implemented for miniAOD... maybe already in?
    objectMtToPfMet_tes  = 'mtMET({object_idx}, "", "pfmet", "tes+" , 1)',
    objectMtToPfMet_jes  = 'mtMET({object_idx}, "", "pfmet", "jes+" , 1)',
    objectMtToPfMet_ues  = 'mtMET({object_idx}, "", "pfmet", "ues+" , 1)',

    #MVA MET
    objectMtToMVAMET     = 'mtMET({object_idx}, "", "mvamet", "", 0)',

    objectToMETDPhi = 'deltaPhi({object}.phi, met().phi())',
)

# Variables based on pairs of objects
pairs = PSet(
    object1_object2_Mass = 'subcand({object1_idx}, {object2_idx}).get.mass',
    object1_object2_Mt = 'subcand({object1_idx}, {object2_idx}).get.mt',
    object1_object2_Pt = 'subcand({object1_idx}, {object2_idx}).get.pt',
    object1_object2_Eta = 'subcand({object1_idx}, {object2_idx}).get.eta',
    object1_object2_Phi = 'subcand({object1_idx}, {object2_idx}).get.phi',
    object1_object2_DR = 'dR({object1_idx}, {object2_idx})',
    object1_object2_DPhi = 'dPhi({object1_idx}, {object2_idx})',
    object1_object2_SS = 'likeSigned({object1_idx}, {object2_idx})',
    object1_object2_PZeta = 'pZeta({object1_idx}, {object2_idx})',
    object1_object2_PZetaVis = 'pZetaVis({object1_idx}, {object2_idx})',
    object1_object2_CosThetaStar = 'abs(subcand({object1_idx}, {object2_idx}).get.daughterCosThetaStar(0))',

    #Pairs + MET
    object1_object2_ToMETDPhi_Ty1 = 'twoParticleDeltaPhiToMEt({object1_idx}, {object2_idx}, "type1")',
)

extraJetPairs = PSet(
    object1_object2_Mass = '? evt.jets.size()>{object2_idx} ? dijetMass({object1_idx},{object2_idx}) : -999'
    #object1_object2_Mass = '? evt.jets.size()>({object2_idx}) ? subcand({object1}, {object2}).get.mass : -999',
    #object1_object2_Mt = '? evt.jets.size()>({object2_idx}) ? subcand({object1}, {object2}).get.mt : -999',
    #object1_object2_Pt = '? evt.jets.size()>({object2_idx}) ? subcand({object1}, {object2}).get.pt : -999',
    #object1_object2_Eta = '? evt.jets.size()>({object2_idx}) ? subcand({object1}, {object2}).get.eta : -999',
    #object1_object2_Phi = '? evt.jets.size()>({object2_idx}) ? subcand({object1}, {object2}).get.phi : -999',
    #object1_object2_DR = '? evt.jets.size()>({object2_idx}) ? dR({object1}, {object2}) : -999',
    #object1_object2_DPhi = '? evt.jets.size()>({object2_idx}) ? dPhi({object1}, {object2}) : -999',
    #object1_object2_Rapidity = '? evt.jets.size()>({object2_idx}) ? subcand({object1}, {object2}).get.rapidity : -999',
)

finalstate = PSet(
    LT = 'ht',
    charge = 'charge',
    Pt = 'pt',
    Eta = 'eta',
    Phi = 'phi',
    Mass = 'mass',
    Mt = 'mt',
    Ht = 'jetHt("pt>30 && abs(eta)<2.5")',
    MassError = 'userFloat("cand_dM")',
    MassErrord1 = 'userFloat("cand_dM_0")',
    MassErrord2 = 'userFloat("cand_dM_1")',
    MassErrord3 = 'userFloat("cand_dM_2")',
    MassErrord4 = 'userFloat("cand_dM_3")'
)


vbf = PSet(
  # If nJets < 2, none of these other branches are valid
   vbfNJets = 'vbfVariables("pt >30").nJets',
   vbfJetVeto30 = 'vbfVariables("pt >30").jets30',
   vbfJetVeto20 = 'vbfVariables("pt >30").jets20',
   vbfJetVetoTight30 = 'vbfVariables("pt >30").jets30',
   vbfJetVetoTight20 = 'vbfVariables("pt >30").jets20',
   vbfMVA = 'vbfVariables("pt >30").mva',
   vbfMass = 'vbfVariables("pt >30").mass',
   vbfDeta = 'vbfVariables("pt >30").deta',
   vbfDphi = 'vbfVariables("pt >30").dphi',
   vbfj1eta = 'vbfVariables("pt >30").eta1',
   vbfj2eta = 'vbfVariables("pt >30").eta2',
   vbfVispt = 'vbfVariables("pt >30").c2',
   vbfHrap = 'vbfVariables("pt >30").hrapidity',
   vbfDijetrap = 'vbfVariables("pt >30").dijetrapidity',
   vbfDphihj = 'vbfVariables("pt >30").dphihj',
   vbfDphihjnomet = 'vbfVariables("pt >30").dphihj_nomet',
   vbfj1pt = 'vbfVariables("pt >30").pt1',
   vbfj2pt = 'vbfVariables("pt >30").pt2',
   vbfdijetpt = 'vbfVariables("pt >30").dijetpt',
   vbfditaupt = 'vbfVariables("pt >30").ditaupt',
)

dijet = PSet(
   object1_object2Mass = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).mass',
   object1_object2Deta = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).deta',
   object1_object2Dphi = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).dphi',
   object1_object2DR = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).dr',
   object1ptLead = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).pt1',
   object2ptSubLead = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).pt2',
   object1etaLead = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).eta1',
   object2etaSubLead = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).eta2',
   object1_object2Dijetrap = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).dijetrapidity',
   object1_object2dijetpt = 'dijetVariables("pt >20&& abs(eta)<2.5",{object1_idx},{object2_idx}).dijetpt',
)


extraJet = PSet(
    objectPt = '? evt.jets.size()>{object_idx} ? {object}.pt() : -999',
    objectEta = '? evt.jets.size()>{object_idx} ? {object}.eta() : -999',
    objectPhi = '? evt.jets.size()>{object_idx} ? {object}.phi() : -999',
    objectPUMVA = '? evt.jets.size()>{object_idx} ? {object}.userFloat("pileupJetId:fullDiscriminant") : -999',
    objectBJetCISV = '? evt.jets.size()>{object_idx} ? {object}.bDiscriminator(\'pfCombinedInclusiveSecondaryVertexV2BJetTags\') : -999',
)

extraJetCandPairs = PSet(
    object1_object2DR = '? evt.jets.size()>{object2_idx} ? dRtoJets({object1_idx}, {object2_idx}) : -999',
)
