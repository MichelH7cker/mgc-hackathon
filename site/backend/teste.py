import requests
from bs4 import BeautifulSoup

# Lista de URLs
urls = [
    "https://docs.magalu.cloud/docs/computing/virtual-machine/overview",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/images/list-images",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/list-instances",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/get-details-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/access-win-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/create-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/create-win-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/gen-ssh-key-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/set-ssh-key-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/delete-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/start-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/stop-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/suspend-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/reboot-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/resize-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/attach-nic-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/rename-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/instances/detach-nic-instance",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/machine-types/list-machines-types",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/snapshots/list-snapshots",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/snapshots/get-details-snapshot",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/snapshots/create-snapshot",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/snapshots/delete-snapshot",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/snapshots/restore-snapshot",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/how-to/snapshots/rename-snapshot",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/additional-explanations/status-and-states",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/additional-explanations/tips-and-flags",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/additional-explanations/pricing",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/offers/offer-image-type",
    "https://docs.magalu.cloud/docs/computing/virtual-machine/offers/offer-instances-type",
    "https://docs.magalu.cloud/docs/storage/object-storage/overview",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/requirements",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/buckets/create-bucket",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/buckets/list-bucket",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/buckets/change-permissions",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/buckets/delete-bucket",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/buckets/delete-bucket-with-objects",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/buckets/copy-url",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/upload-object",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/upload-dir",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/list-objects",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/download-object",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/download-all-objects",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/delete-object",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/delete-all-objects",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/copy-url-object",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/public-object",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/objects/public-existent-object",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/acl/create-acl",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/versioning/verify-versioning",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/versioning/activate-versioning-bucket",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/versioning/list-versions",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/bucket-policy/",
    "https://docs.magalu.cloud/docs/storage/object-storage/how-to/terraform/tofu",
    "https://docs.magalu.cloud/docs/storage/object-storage/compatible-tools/",
    "https://docs.magalu.cloud/docs/storage/object-storage/compatible-tools/mgc-cli-compatibility",
    "https://docs.magalu.cloud/docs/storage/object-storage/storage-classes/standard",
    "https://docs.magalu.cloud/docs/storage/object-storage/storage-classes/cold-storage",
    "https://docs.magalu.cloud/docs/storage/object-storage/storage-classes/overview",
    "https://docs.magalu.cloud/docs/storage/object-storage/access-control/overview",
    "https://docs.magalu.cloud/docs/storage/object-storage/use-cases/storage-midia-content",
    "https://docs.magalu.cloud/docs/storage/object-storage/use-cases/clipshare",
    "https://docs.magalu.cloud/docs/storage/object-storage/use-cases/backups",
    "https://docs.magalu.cloud/docs/storage/object-storage/additional-explanations/price",
    "https://docs.magalu.cloud/docs/storage/object-storage/additional-explanations/security",
    "https://docs.magalu.cloud/docs/storage/object-storage/additional-explanations/product-limits",
    "https://docs.magalu.cloud/docs/storage/object-storage/additional-explanations/glossary",
    "https://docs.magalu.cloud/docs/storage/object-storage/troubleshooting/upload-small-files",
    "https://docs.magalu.cloud/docs/storage/object-storage/troubleshooting/delete-large-bucket",
    "https://docs.magalu.cloud/docs/storage/object-storage/troubleshooting/bucket-permission",
    "https://docs.magalu.cloud/docs/storage/object-storage/troubleshooting/name-rules",
    "https://docs.magalu.cloud/docs/storage/object-storage/troubleshooting/velero-config",
    "https://docs.magalu.cloud/docs/storage/block-storage/overview",
    "https://docs.magalu.cloud/docs/storage/block-storage/how-to/volumes/list-volume",
    "https://docs.magalu.cloud/docs/storage/block-storage/how-to/volume-types/list-volume-types",
    "https://docs.magalu.cloud/docs/storage/block-storage/how-to/snapshots/list-snapshots",
    "https://docs.magalu.cloud/docs/storage/block-storage/how-to/snapshots/create-snapshot",
    "https://docs.magalu.cloud/docs/storage/block-storage/additional-explanations/tips-and-flags",
    "https://docs.magalu.cloud/docs/storage/block-storage/additional-explanations/naming-rules",
    "https://docs.magalu.cloud/docs/storage/block-storage/additional-explanations/pricing",
    "https://docs.magalu.cloud/api/block-storage#tag/volumes/operation/list_volume_v1_v1_volumes_get",
    "https://docs.magalu.cloud/docs/dbaas/overview",
    "https://docs.magalu.cloud/docs/dbaas/how-to/create-instance",
    "https://docs.magalu.cloud/docs/dbaas/how-to/connect-to-dbaas",
    "https://docs.magalu.cloud/docs/dbaas/how-to/change-parameter-configurations",
    "https://docs.magalu.cloud/docs/dbaas/how-to/manage-users-permissions",
    "https://docs.magalu.cloud/docs/dbaas/how-to/backup-restore",
    "https://docs.magalu.cloud/docs/dbaas/how-to/solve-common-problems",
    "https://docs.magalu.cloud/docs/dbaas/how-to/identify-problems",
    "https://docs.magalu.cloud/docs/dbaas/how-to/migrate-db-to-cloud",
    "https://docs.magalu.cloud/docs/dbaas/how-to/resize-volume-machine-type",
    "https://docs.magalu.cloud/docs/dbaas/how-to/create-manage-db-replicas",
    "https://docs.magalu.cloud/docs/dbaas/tutorials/add-monitor-mysql-prometheus-grafana",
    "https://docs.magalu.cloud/docs/dbaas/additional-explanations/naming-rules",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/overview",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/how-to/clusters/requirements",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/how-to/clusters/create-cluster",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/how-to/clusters/cluster-autoscaling",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/how-to/persistent-volumes/create-persistent-volumes",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/tutorials/create-deployment",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/tutorials/restrict-acess-loadbalancer",
    "https://docs.magalu.cloud/docs/containers-manager/kubernetes/additional-explanations/naming-rules",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/overview",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/how-to/requirements",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/how-to/download-and-install",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/how-to/auth",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/how-to/admin-workspace",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/how-to/admin-tenants",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/how-to/config",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/login",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/access_token",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/clients/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/clients/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/clients/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/clients/update",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/tenant/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/tenant/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/tenant/current",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/auth/tenant/set",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/delete",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/rename",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/snapshots/restore",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volume-attachment/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volume-attachment/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volume-attachment/delete",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volume-attachment/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volume-types/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volume-types/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/block-storage/volumes/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/config/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/config/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/config/delete",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/config/get-schema",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/config/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/config/set",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/credentials/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/credentials/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/images/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/images/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/images/delete",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/images/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/registries/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/registries/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/registries/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/registries/delete",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/registries/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/repositories/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/repositories/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/repositories/delete",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/container-registry/repositories/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/backups/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/datastores/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/datastores/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/engines/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/engines/get",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/flavors/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/instances/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/instances/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/instances/backups/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/instances/backups/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/replicas/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/replicas/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/dbaas/replicas/start",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/http/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/http/do",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/http/json/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/kubernetes/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/network/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/buckets/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/buckets/create",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/buckets/acl/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/buckets/versioning/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/key-pair/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/object-storage/objects/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/profile/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/virtual-machine/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/virtual-machine/images/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/virtual-machine/images/list",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/virtual-machine/instances/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/virtual-machine/machine-types/help",
    "https://docs.magalu.cloud/docs/devops-tools/cli-mgc/commands-reference/virtual-machine/snapshots/help",
    "https://docs.magalu.cloud/docs/devops-tools/api-keys/overview",
    "https://docs.magalu.cloud/docs/devops-tools/api-keys/how-to/object-storage/create-api-keys",
    "https://docs.magalu.cloud/docs/devops-tools/api-keys/how-to/object-storage/query-api-keys",
    "https://docs.magalu.cloud/docs/devops-tools/api-keys/how-to/other-products/create-api-key",
    "https://docs.magalu.cloud/docs/devops-tools/apis/auth",
    "https://docs.magalu.cloud/docs/devops-tools/apis/pagination-filters-orders",
    "https://docs.magalu.cloud/docs/devops-tools/apis/tenand-id",
    "https://docs.magalu.cloud/docs/devops-tools/apis/virtual-machines",
    "https://docs.magalu.cloud/docs/devops-tools/apis/audit",
    "https://docs.magalu.cloud/docs/devops-tools/apis/network",
    "https://docs.magalu.cloud/docs/devops-tools/apis/block-storage",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/overview",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/examples",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/requirements",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/download-setup",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/provider-region",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/auth",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/add-resources",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/env-variables",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/testing-terraform",
    "https://docs.magalu.cloud/docs/devops-tools/terraform/how-to/complete-docs",
    "https://docs.magalu.cloud/docs/devops-tools/general/env-variables",
    "https://docs.magalu.cloud/docs/profile/ssh-keys/overview",
    "https://docs.magalu.cloud/docs/profile/ssh-keys/how-to/create",
    "https://docs.magalu.cloud/docs/profile/ssh-keys/how-to/get-list",
    "https://docs.magalu.cloud/docs/profile/audit/overview",
    "https://docs.magalu.cloud/docs/profile/audit/how-to/list-events",
    "https://docs.magalu.cloud/docs/profile/audit/how-to/list-event-types",
    "https://docs.magalu.cloud/docs/profile/audit/additional-explanations/tips-and-flags",
    "https://docs.magalu.cloud/docs/profile/audit/additional-explanations/products-that-emit-events",
    "https://docs.magalu.cloud/docs/profile/audit/additional-explanations/events-specification",
    "https://docs.magalu.cloud/docs/billing/bss/overview",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/calculate-cost-using-services",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/payments-methods",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/controlling-expenses",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/discount-credit-polices",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/invoices",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/invoices",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/decimal-places",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/installment-invoices",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/upgrade-downgrade-products",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/period-calculating-invoice",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/update-value-invoice-screen",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/update-value-invoice-screen",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/update-info-my-account",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/refund-policy-cancelation",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/additional-fee-late-payments",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/detailed-summary-resource-consumption",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/credit-card-charge",
    "https://docs.magalu.cloud/docs/billing/bss/additional-explanations/variation-dolar-exchange-rate",
    "https://docs.magalu.cloud/docs/preview-program/public-preview-2408"
]

# Arquivo de saída
with open("documentacao.txt", "w", encoding="utf-8") as file:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Seleciona o conteúdo dentro da div desejada
        content_div = soup.find('div', class_='theme-doc-markdown markdown')
        if content_div:
            file.write(content_div.get_text())
            file.write("\n\n---\n\n")  # Separador entre conteúdos