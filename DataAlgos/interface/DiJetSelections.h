/*
 * Get DiJet distributions for an arbitrary pair of jets in the event
 *
 * Based on VBF Selections implementation
 *
 */

#ifndef DIJETSELECTIONS_9N7EKFZ2
#define DIJETSELECTIONS_9N7EKFZ2

#include <vector>
#include "DataFormats/Candidate/interface/Candidate.h"
#include "FinalStateAnalysis/DataAlgos/interface/DiJetVariables.h"

DiJetVariables computeDiJetInfo(
    const std::vector<const reco::Candidate*>& hardScatter,
    const reco::Candidate::LorentzVector& metp4,
    const std::vector<const reco::Candidate*>& jets,
    const unsigned int firstJet,
    const unsigned int secondJet);

#endif /* end of include guard: DIJETSELECTIONS_9N7EKFZ2 */
