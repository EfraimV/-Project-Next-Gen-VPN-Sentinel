resource "aws_ec2_client_vpn_endpoint" "secure" {
  description            = "Zero-Trust VPN"
  server_certificate_arn = aws_acm_certificate.vpn.arn
  split_tunnel           = false  # Force all traffic through VPN
  
  authentication_options {
    type              = "certificate-authentication"
    root_certificate_chain_arn = aws_acm_certificate.root.arn
  }

  connection_log_options {
    enabled               = true
    cloudwatch_log_group  = aws_cloudwatch_log_group.vpn.name
  }
}
