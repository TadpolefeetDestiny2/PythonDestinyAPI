import requests

my_headers = {'X-API-Key': 'APIKEY'}
destiny_Membership_Id = 4611686018484802398
membershipId = 21713117



def ChoosePlatform(types):
    bungie_membership_type = {
      'None': "0",
      'TigerXbox': "1",
      'TigerPSN': "2",
      'TigerSteam': "3",
      'TigerBlizzard': "4",
      'TigerStadia': "5",
      'TigerDemon': "10",
      'BungieNext': "254",
      'All': "-1",
      'Steam': "3"
    }
    return bungie_membership_type[types]


def ChooseParameters(types):
    destiny_component_type = {
        'None': "0",
        'Profiles': "100",
        'VendorReceipts': "101",
        'ProfileInventories': "102",
        'ProfileCurrencies': "103",
        'ProfileProgression': "104",
        'PlatformSilver': "105",
        'Characters': "200",
        'CharacterInventories': "201",
        'CharacterProgressions': "202",
        'CharacterRenderData': "203",
        'CharacterActivities': "204",
        'CharacterEquipment': "205",
        'ItemInstances': "300",
        'ItemObjectives': "301",
        'ItemPerks': "302",
        'ItemRenderData': "303",
        'ItemStats': "304",
        'ItemSockets': "305",
        'ItemTalentGrids': "306",
        'ItemCommonData': "307",
        'ItemPlugStates': "308",
        'ItemPlugObjectives': "309",
        'ItemReusablePlugs': "310",
        'Vendors': "400",
        'VendorCategories': "401",
        'VendorSales': "402",
        'Kiosks': "500",
        'CurrencyLookups': "600",
        'PresentationNodes': "700",
        'Collectibles': "800",
        'Records': "900",
        'Transitory': "1000",
        'Metrics': "1100",
        'StringVariables': "1200"
    }
    return f'?components={destiny_component_type[types]}'

def GetDestinyManifest(parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Manifest/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetDestinyEntityDefinition(entityType, hashIdentifier, parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Manifest/{entityType}/{hashIdentifier}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def SearchDestinyPlayer(platform, displayName, parameters):
    membershipType = ChoosePlatform(platform)
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/{membershipType}/{displayName}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetLinkedProfiles(platform, membershipId, parameters):
    membershipType = ChoosePlatform(platform)
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetProfile(platform, destinyMembershipId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetCharacter(platform, destinyMembershipId, characterId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetClanWeeklyRewardState(groupId, parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Clan/{groupId}/WeeklyRewardState/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetItem(platform, destinyMembershipId, itemInstanceId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetVendors(platform, destinyMembershipId, characterId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetVendor(platform, destinyMembershipId, characterId, vendorHash, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetCollectibleNodeDetails(platform, destinyMembershipId, characterId, collectiblePresentationNodeHash, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/{collectiblePresentationNodeHash}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetPostGameCarnageReport(activityId, parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Stats/PostGameCarnageReport/{activityId}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetHistoricalStatsDefinition(parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Stats/Definition/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def SearchDestinyEntities(type, searchTerm, parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Armory/Search/{type}/{searchTerm}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetHistoricalStats(platform, destinyMembershipId, characterId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetHistoricalStatsForAccount(platform, destinyMembershipId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetActivityHistory(platform, destinyMembershipId, characterId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetUniqueWeaponHistory(platform, destinyMembershipId, characterId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetDestinyAggregateActivityStats(platform, destinyMembershipId, characterId, parameters):
    membershipType = ChoosePlatform(platform)
    if destinyMembershipId == "None":
        destinyMembershipId = destiny_Membership_Id
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetPublicMilestoneContent(milestoneHash, parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Milestones/{milestoneHash}/Content/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def GetPublicMilestones(parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Milestones/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text


def AwaGetActionToken(correlationId, parameters):
    response = requests.get(f"https://www.bungie.net/Platform/Destiny2/Awa/GetActionToken/{correlationId}/{ChooseParameters(parameters)}", headers=my_headers)
    return response.text
