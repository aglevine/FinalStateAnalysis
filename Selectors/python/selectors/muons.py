import FWCore.ParameterSet.Config as cms

id = cms.PSet(
    name = cms.string("${name}_MuID"),
    description = cms.string("$nicename Muon ID [${muID}]"),
    cut = cms.string("${getter}userInt('${muID}') > 0.5"),
    plottable = cms.string("${getter}userInt('${muID}')"),
    invert = cms.bool(False),
)

reliso = cms.PSet(
    name = cms.string("${name}_RelIsoDB"),
    description = cms.string("$nicename #Delta#Beta Rel. Iso [${threshold}]"),
    cut = cms.string(
        "(${getter}chargedHadronIso"
        "+max(${getter}photonIso()"
        "+${getter}neutralHadronIso()"
        "-0.5*${getter}userIso(0),0.0))"
        "/${getter}pt() < ${threshold}"
    ),
    plottable = cms.string(
        "(${getter}chargedHadronIso"
        "+max(${getter}photonIso()"
        "+${getter}neutralHadronIso()"
        "-0.5*${getter}userIso(0),0.0))"
        "/${getter}pt()"
    ),
    invert = cms.bool(False)
)

################################################################################
### Trigger match selectors  ###################################################
################################################################################

# For HLT_Mu13_Mu8
hltSingleMu13L3Filtered13 = cms.PSet(
    name = cms.string("${name}_hltSingleMu13L3Filtered13"),
    description = cms.string("$nicename trigger match hltSingleMu13L3Filtered13"),
    cut = cms.string(
        'matchToHLTFilter(${index}, "hltSingleMu13L3Filtered13")'
    ),
    plottable = cms.string(
        'matchToHLTFilter(${index}, "hltSingleMu13L3Filtered13")'
    ),
    invert = cms.bool(False)
)

# For HLT_Mu13_Mu8
hltDiMuonL3p5PreFiltered8 = cms.PSet(
    name = cms.string("${name}_hltDiMuonL3p5PreFiltered8"),
    description = cms.string("$nicename trigger match hltDiMuonL3p5PreFiltered8"),
    cut = cms.string(
        'matchToHLTFilter(${index}, "hltDiMuonL3(p5|)PreFiltered8")'
    ),
    plottable = cms.string(
        'matchToHLTFilter(${index}, "hltDiMuonL3(p5|)PreFiltered8")'
    ),
    invert = cms.bool(False)
)

# For HLT_DoubleMu7
hltDiMuonL3PreFiltered7 = cms.PSet(
    name = cms.string("${name}_hltDiMuonL3PreFiltered7"),
    description = cms.string("$nicename trigger match hltDiMuonL3PreFiltered7"),
    cut = cms.string(
        'matchToHLTFilter(${index}, "hltDiMuonL3PreFiltered7")'
    ),
    plottable = cms.string(
        'matchToHLTFilter(${index}, "hltDiMuonL3PreFiltered7")'
    ),
    invert = cms.bool(False)
)

# For Mu30
hltSingleMu30L3Filtered30 = cms.PSet(
    name = cms.string("${name}_hltSingleMu30L3Filtered30"),
    description = cms.string("$nicename trigger match (hltSingleMu30L3Filtered30) HLT_Mu30"),
    cut = cms.string(
        r'matchToHLTFilter(${index}, "hltSingleMu30(L2Qual|)L3Filtered30")'
    ),
    plottable = cms.string(
        r'matchToHLTFilter(${index}, "hltSingleMu30(L2Qual|)L3Filtered30")'
    ),
    invert = cms.bool(False)
)

# For IsoMu24
# hltSingleMu(L2Qual|)IsoL3IsoFiltered24
hltSingleMuIsoL3IsoFiltered24 = cms.PSet(
    name = cms.string("${name}_hltSingleMuIsoL3IsoFiltered24"),
    description = cms.string("$nicename trigger match (hltSingleMuIsoL3IsoFiltered24) HLT_IsoMu24"),
    cut = cms.string(
        r'matchToHLTFilter(${index}, "hltSingleMu(L2Qual|)IsoL3IsoFiltered24")'
    ),
    plottable = cms.string(
        r'matchToHLTFilter(${index}, "hltSingleMu(L2Qual|)IsoL3IsoFiltered24")'
    ),
    invert = cms.bool(False)
)

# For Mu8_Ele17
hltL1Mu3EG5L3Filtered8 = cms.PSet(
    name = cms.string("${name}_hltL1Mu3EG5L3Filtered8"),
    description = cms.string("$nicename trigger match (hltL1Mu3EG5L3Filtered8 ) HLT_Mu8_Ele17"),
    cut = cms.string(
        r'matchToHLTFilter(${index}, "hltL1Mu3EG5L3Filtered8")'
    ),
    plottable = cms.string(
        r'matchToHLTFilter(${index}, "hltL1Mu3EG5L3Filtered8")'
    ),
    invert = cms.bool(False)
)

# For Mu17_Ele8
hltL1Mu3EG5L3Filtered17 = cms.PSet(
    name = cms.string("${name}_hltL1Mu3EG5L3Filtered17"),
    description = cms.string("$nicename trigger match (hltL1Mu3EG5L3Filtered17) HLT_Mu17_Ele8"),
    cut = cms.string(
        r'matchToHLTFilter(${index}, "hltL1Mu3EG5L3Filtered17")'
    ),
    plottable = cms.string(
        r'matchToHLTFilter(${index}, "hltL1Mu3EG5L3Filtered17")'
    ),
    invert = cms.bool(False)
)

## For HLT_IsoMu24_vX
#HLT_IsoMu24 = cms.PSet(
    #name = cms.string("${name}_HLT_IsoMu24"),
    #description = cms.string("$nicename trigger match HLT_IsoMu24"),
    #cut = cms.string(
        #r'matchToHLTPath(${index}, "HLT_IsoMu24_v\\d+")'
    #),
    #plottable = cms.string(
        #r'matchToHLTPath(${index}, "HLT_IsoMu24_v\\d+")'
    #),
    #invert = cms.bool(False)
#)

## For HLT_IsoMu24_vX
#HLT_IsoMu17 = cms.PSet(
    #name = cms.string("${name}_HLT_IsoMu17"),
    #description = cms.string("$nicename trigger match HLT_IsoMu17"),
    #cut = cms.string(
        #r'matchToHLTPath(${index}, "HLT_IsoMu17_v\\d+")'
    #),
    #plottable = cms.string(
        #r'matchToHLTPath(${index}, "HLT_IsoMu17_v\\d+")'
    #),
    #invert = cms.bool(False)
#)

## For HLT_Mu15_vX
#HLT_Mu15 = cms.PSet(
    #name = cms.string("${name}_HLT_Mu15"),
    #description = cms.string("$nicename trigger match HLT_Mu15"),
    #cut = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu15_v\\d+")'
    #),
    #plottable = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu15_v\\d+")'
    #),
    #invert = cms.bool(False)
#)

#HLT_Mu30 = cms.PSet(
    #name = cms.string("${name}_HLT_Mu30"),
    #description = cms.string("$nicename trigger match HLT_Mu30"),
    #cut = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu30_v\\d+")'
    #),
    #plottable = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu30_v\\d+")'
    #),
    #invert = cms.bool(False)
#)


## For HLT Mu17 Ele8.
#HLT_Mu17_Ele8 = cms.PSet(
    #name = cms.string("${name}_HLT_Mu17_Ele8"),
    #description = cms.string("$nicename trigger match HLT_Mu17_Ele8"),
    #cut = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu17_Ele8_CaloId(T|L)(_CaloIsoVL|)_v\\d+")'
    #),
    #plottable = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu17_Ele8_CaloId(T|L)(_CaloIsoVL|)_v\\d+")'
    #),
    #invert = cms.bool(False)
#)

## For HLT Mu8 Ele17.
#HLT_Mu8_Ele17 = cms.PSet(
    #name = cms.string("${name}_HLT_Mu8_Ele17"),
    #description = cms.string("$nicename trigger match HLT_Mu8_Ele17"),
    #cut = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu8_Ele17_CaloId(T|L)(_CaloIsoVL|)_v\\d+")'
    #),
    #plottable = cms.string(
        #r'matchToHLTPath(${index}, "HLT_Mu8_Ele17_CaloId(T|L)(_CaloIsoVL|)_v\\d+")'
    #),
    #invert = cms.bool(False)
#)
