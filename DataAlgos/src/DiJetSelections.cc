#include "FinalStateAnalysis/DataAlgos/interface/DiJetSelections.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

DiJetVariables computeDiJetInfo(
    const std::vector<const reco::Candidate*>& hardScatter,
    const reco::Candidate::LorentzVector& metp4,
    const std::vector<const reco::Candidate*>& jets,
    const unsigned int firstJet,
    const unsigned int secondJet) {
  DiJetVariables output;

  // number of initial jets
  output.nJets = jets.size();

  // Not enough jets
  if (output.nJets <= secondJet)
    return output;

  //assert(jets[0]->pt() > jets[1]->pt());
  
  output.leadJet = jets[firstJet];
  output.subleadJet = jets[secondJet];
    
  // Get 4vectors of two highest jets
  reco::Candidate::LorentzVector leadJet(output.leadJet->p4());
  reco::Candidate::LorentzVector subleadJet(output.subleadJet->p4());

  reco::Candidate::LorentzVector dijet = leadJet + subleadJet;


  output.mass = dijet.mass();
  output.deta = std::abs(leadJet.eta() - subleadJet.eta());
  output.dphi = std::abs(reco::deltaPhi(leadJet.phi(), subleadJet.phi()));
  output.dr = reco::deltaR(leadJet.eta(),leadJet.phi(),subleadJet.eta(),subleadJet.phi());
  output.pt1 = leadJet.pt();
  output.pt2 = subleadJet.pt();
  output.dijetpt = dijet.pt();
  output.dijetrapidity = dijet.Rapidity();
  output.eta1 = leadJet.eta();
  output.eta2 = subleadJet.eta();
 
  return output;
}
