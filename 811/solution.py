class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_count = {}
        for domains in cpdomains:
            count, domain = domains.split(" ")
            parts = domain.split(".")

            for i in range(len(parts)):
                sub = ".".join(parts[i:])
                subdomain_count[sub] = subdomain_count.get(sub, 0) + int(count)
        # build result list from counts dict as "count domain" strings
        return [f"{total} {subdomain}" for subdomain, total in subdomain_count.items()]
