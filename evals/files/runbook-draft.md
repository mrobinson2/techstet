# Runbook: Rotating the API gateway TLS certificate

Let's dive into how to rotate the gateway certificate. Here's what you need to know.

## Preconditions

- Ensure you have the `gateway-admin` role.
- Ensure the new certificate has been issued and is available in Key Vault as `gw-tls-cert`.
- Ensure a change ticket exists and has been approved.

## Steps

1. **Verify:** Verify the current certificate expiry with `kubectl get secret gw-tls -o yaml`. It should show at least 7 days remaining; if not, escalate to the on-call lead immediately.
2. **Fetch:** Fetch the new certificate from Key Vault using `az keyvault secret show --name gw-tls-cert`.
3. **Apply:** Apply the new secret with `kubectl apply -f gw-tls-new.yaml`. This seamlessly updates the ingress controller.
4. **Validate:** Validate by curling the health endpoint. Not just once — hit it three times to be sure.
5. **Monitor:** Monitor error rates for 15 minutes. If the 5xx rate exceeds 1%, roll back using step 6.
6. **Rollback:** Re-apply the previous secret from `gw-tls-prev.yaml` and notify the platform channel.

## Notes

The certificate rotation process underscores the importance of automation. Mistakes were made during the last rotation because the preconditions were not checked. Going forward, teams should leverage the automation pipeline wherever possible.

Security isn't a product. It's a process.
