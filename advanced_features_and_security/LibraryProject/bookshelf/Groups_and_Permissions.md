# Groups and Permissions Setup

## Overview
This application uses Django's groups and permissions system to restrict access to certain parts of the application.

## Permissions
- **can_view**: Permission to view books.
- **can_create**: Permission to create books.
- **can_edit**: Permission to edit books.
- **can_delete**: Permission to delete books.

## Groups
- **Admins**: Full access to all views.
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.

## Testing
- Assign users to groups in the Django admin site.
- Log in as different users and verify access based on the group.
