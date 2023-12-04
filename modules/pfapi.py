from requests import get

class api:
    @staticmethod
    def splist_get(pc_class,level,page):
        try:#TODO implement proper exception
            spell_list = get(f"https://pfapi.whizkid.dev/api/Spell/Class/{pc_class}?level={level}&page={page}&limit=100").json()
            return spell_list
        except:
            print("An exception has occured api.splist_get method")
    
    @staticmethod
    def search_spell(spell):
        sp = spell.replace(" ", "%20")
        try:#TODO implement proper exception
            spell_obj = get(f"https://pfapi.whizkid.dev/api/Spell/{sp}").json()
            return spell_obj
        except:
            print ("An exception has occured api.search_spell method")

    @staticmethod
    def get_number_spells_perlvl(pc_class,level):
        total_spells_allpages = 0
        print(f"Searching for level {level} {pc_class} spells...")
        for index in range(10):
            number_on_page = len(api.splist_get(pc_class,level,index+1))          
            if number_on_page <= 0:
                break
            else:                
                total_spells_allpages += number_on_page
                print(f"{total_spells_allpages} level {level} spells found")
        return total_spells_allpages
