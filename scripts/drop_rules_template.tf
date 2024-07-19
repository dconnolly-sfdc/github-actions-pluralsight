resource "newrelic_nrql_drop_rule" "foo" {
  account_id  = 12345
  description = "Drops all data for MyCustomEvent that comes from the LoadGeneratingApp in the dev environment, because there is too much and we don’t look at it."
  action      = "drop_data"
  nrql        = "SELECT * FROM MyCustomEvent WHERE appName='{{application_name}}'"
}
