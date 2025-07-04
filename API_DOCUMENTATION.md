# Comprehensive API Documentation

## Table of Contents
1. [Overview](#overview)
2. [Python Scripts](#python-scripts)
3. [OpenAPI Specifications](#openapi-specifications)
4. [Postman Collections](#postman-collections)
5. [Usage Examples](#usage-examples)
6. [Setup and Installation](#setup-and-installation)

## Overview

This repository contains a collection of Python scripts for AWS operations, OpenAPI specifications for various services, and Postman collections for API testing. The primary focus is on server scripting and API management.

---

## Python Scripts

### 1. AWS S3 Scripting (`s3ripting.py`)

**Purpose**: Creates AWS S3 buckets with specified configurations.

#### Functions

##### S3 Bucket Creation
```python
import boto3

s3 = boto3.resource('s3')
bucket_name = "BucketMRaj"
response = s3.create_bucket(
    Bucket=bucket_name, 
    CreateBucketConfiguration={'LocationConstraint':'us-east-2'}
)
```

**Parameters:**
- `bucket_name` (string): Name of the S3 bucket to create
- `LocationConstraint` (string): AWS region for bucket creation

**Returns:**
- `response`: S3 bucket creation response object

**Usage Example:**
```python
try:
    response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
    print(response)
except Exception as error:
    print(error)
```

**Requirements:**
- AWS credentials configured
- `boto3` library installed
- Appropriate S3 permissions

---

### 2. AWS EC2 Scripting (`AWScripting.py`)

**Purpose**: Manages AWS EC2 instances, specifically for termination operations.

#### Functions

##### EC2 Instance Termination
```python
import boto3

ec2 = boto3.resource('ec2')
instance_id = 'i-0837712bae72e34db'
instance = ec2.Instance(instance_id)
response = instance.terminate()
```

**Parameters:**
- `instance_id` (string): EC2 instance identifier

**Returns:**
- `response`: Instance termination response object

**Usage Example:**
```python
import boto3

ec2 = boto3.resource('ec2')
instance_id = 'i-0837712bae72e34db'
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)
```

**Requirements:**
- AWS credentials configured
- `boto3` library installed
- EC2 management permissions

---

### 3. Hello World Test (`helloWorld.py`)

**Purpose**: Simple test file for synchronization verification.

**Content:**
```json
{
    "details": "Sync success"
}
```

**Usage**: Used for testing deployment and synchronization processes.

---

## OpenAPI Specifications

### 1. Baidethi User API (`SchemaSync_March/Mandark`)

**Base URL**: `http://localhost:3000`
**Version**: 1.1.1

#### Endpoints

##### GET /user
**Summary**: Returns details about a particular user

**Parameters:**
- `id` (query, required): ID of the user (integer, int32)

**Request Example:**
```bash
curl -X GET "http://localhost:3000/user?id=123"
```

**Response (200):**
```json
{
  "id": 123,
  "name": "John Doe",
  "tag": "active"
}
```

**Error Response (default):**
```json
{
  "code": 400,
  "message": "User not found"
}
```

**Components:**
- **User Object**: 
  - `id` (integer, int64, required)
  - `name` (string, required)
  - `tag` (string, optional)

---

### 2. Pet Store API (`Mandark/Dee.dee` & `Mandark/Paul Robertson`)

**Base URL**: `http://petstore.swagger.io/v1`
**Version**: 1.0.0

#### Endpoints

##### GET /pets
**Summary**: List all pets

**Parameters:**
- `limit` (query, optional): How many items to return at one time (max 100, integer)

**Request Example:**
```bash
curl -X GET "http://petstore.swagger.io/v1/pets?limit=10"
```

**Response (200):**
```json
[
  {
    "id": 1,
    "name": "Fluffy",
    "tag": "cat"
  }
]
```

##### POST /pets
**Summary**: Create a new pet

**Request Example:**
```bash
curl -X POST "http://petstore.swagger.io/v1/pets" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Buddy",
    "tag": "dog"
  }'
```

**Response (201):**
```json
{
  "message": "Pet created successfully"
}
```

##### GET /pets/{petId}
**Summary**: Info for a specific pet

**Parameters:**
- `petId` (path, required): The id of the pet (string)

**Request Example:**
```bash
curl -X GET "http://petstore.swagger.io/v1/pets/1"
```

**Response (200):**
```json
{
  "id": 1,
  "name": "Fluffy",
  "tag": "cat"
}
```

---

### 3. OMS Trading API (`Chudamani/Postman Collections/Updated`)

**Base URL**: `http://localhost:3001`
**Version**: v1

#### Endpoints

##### GET /v1/orders
**Summary**: Get orders

**Parameters:**
- `exchange_id` (query, optional): Exchange name (string, example: KRAKEN)

**Request Example:**
```bash
curl -X GET "http://localhost:3001/v1/orders?exchange_id=KRAKEN"
```

**Response (200):**
```json
[
  {
    "type": "snapshotOrders",
    "exchange_name": "KRAKEN",
    "data": [
      {
        "exchange_id": "KRAKEN",
        "id": "KPP-222389382-AQ",
        "client_order_id_format_exchange": "f81211e2-27c4-b86a-8143-01088ba9222c",
        "exchange_order_id": "90832ASASAS89789-1112",
        "amount_open": 0.22,
        "amount_filled": 0.00,
        "status": "REJECTED",
        "symbol_exchange": "BTCUSD",
        "symbol_coinapi": "KRAKEN_SPOT_BTC_USD",
        "amount_order": 0.045,
        "price": 0.0783,
        "side": "BUY",
        "order_type": "LIMIT"
      }
    ]
  }
]
```

##### POST /v1/orders
**Summary**: Create new order

**Request Body:**
```json
{
  "exchange_id": "KRAKEN",
  "client_order_id": "KPP-222389382-AQ",
  "symbol_exchange": "BTCUSD",
  "symbol_coinapi": "KRAKEN_SPOT_BTC_USD",
  "amount_order": 0.045,
  "price": 0.0783,
  "side": "BUY",
  "order_type": "LIMIT",
  "time_in_force": "GOOD_TILL_CANCEL"
}
```

**Request Example:**
```bash
curl -X POST "http://localhost:3001/v1/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "exchange_id": "KRAKEN",
    "client_order_id": "KPP-222389382-AQ",
    "symbol_exchange": "BTCUSD",
    "amount_order": 0.045,
    "price": 0.0783,
    "side": "BUY",
    "order_type": "LIMIT"
  }'
```

##### POST /v1/orders/cancel
**Summary**: Cancel order

**Request Body:**
```json
{
  "exchange_id": "KRAKEN",
  "exchange_order_id": "d8574207d9e3b16a4a5511753eeef1751",
  "client_order_id": "A12345"
}
```

##### POST /v1/orders/cancel/all
**Summary**: Cancel all orders

**Request Body:**
```json
{
  "exchange_id": "KRAKEN"
}
```

##### GET /v1/balances
**Summary**: Get balances

**Parameters:**
- `exchange_id` (query, optional): Exchange name (string, example: KRAKEN)

**Response (200):**
```json
[
  {
    "type": "snapshotBalances",
    "exchange_name": "KRAKEN",
    "data": [
      {
        "id": "BTC",
        "symbol_exchange": "BTC",
        "symbol_coinapi": "BTC",
        "balance": 0.00134444,
        "available": 0.00134444,
        "locked": 0.00000,
        "update_origin": "EXCHANGE"
      }
    ]
  }
]
```

##### GET /v1/positions
**Summary**: Get positions

**Parameters:**
- `exchange_id` (query, optional): Exchange name (string, example: KRAKEN)

---

## Postman Collections

### 1. Sarkari Collection (`PunyaKoti/Github_post.json`)

#### Endpoints

##### Nataru (GET Request)
- **Method**: GET
- **URL**: `https://postman-echo.com/get`
- **Test**: Response time validation (< 300ms)

**Usage:**
```javascript
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(300);
});
```

##### ASN (POST Request)
- **Method**: POST
- **URL**: `https://postman-echo.com/post`

### 2. Postman Echo Collection (`Postman Collections/New_Echo.json`)

Comprehensive collection for testing REST clients with various authentication methods:

#### Authentication Methods

##### Basic Auth
- **Endpoint**: `https://postman-echo.com/basic-auth`
- **Method**: GET
- **Credentials**: username: `postman`, password: `password`

**Usage:**
```bash
curl -X GET "https://postman-echo.com/basic-auth" \
  -u "postman:password"
```

##### Digest Auth
- **Endpoint**: `https://postman-echo.com/digest-auth`
- **Method**: GET
- **Authentication**: Digest authentication

##### Hawk Auth
- **Endpoint**: `https://postman-echo.com/auth/hawk`
- **Method**: GET
- **Hawk Auth ID**: `dh37fgj492je`
- **Hawk Auth Key**: `werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn`

##### OAuth 1.0
- **Endpoint**: `https://postman-echo.com/oauth1`
- **Method**: GET
- **Consumer Key**: `RKCGzna7bv9YD57c`
- **Consumer Secret**: `D+EdQ-gs$-%@2Nu7`

---

## Usage Examples

### Setting up AWS Credentials

```bash
# Install AWS CLI
pip install awscli

# Configure credentials
aws configure
```

### Running Python Scripts

```bash
# Install dependencies
pip install boto3

# Run S3 script
python s3ripting.py

# Run EC2 script
python AWScripting.py
```

### Testing APIs with curl

```bash
# Test user endpoint
curl -X GET "http://localhost:3000/user?id=123" \
  -H "Content-Type: application/json"

# Create order
curl -X POST "http://localhost:3001/v1/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "exchange_id": "KRAKEN",
    "symbol_exchange": "BTCUSD",
    "amount_order": 0.045,
    "price": 0.0783,
    "side": "BUY",
    "order_type": "LIMIT"
  }'
```

### Importing Postman Collections

1. Open Postman
2. Click "Import"
3. Select the JSON files from the collections directory
4. Configure environment variables if needed

---

## Setup and Installation

### Prerequisites

- Python 3.7+
- AWS Account (for AWS scripts)
- Postman (for API testing)

### Installation Steps

1. **Clone the repository:**
```bash
git clone <repository-url>
cd <repository-name>
```

2. **Install Python dependencies:**
```bash
pip install boto3
```

3. **Configure AWS credentials:**
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your default region (e.g., us-east-2)
# Enter output format (json)
```

4. **Import Postman Collections:**
- Open Postman
- Import collections from `Postman Collections/` directory
- Import collections from `PunyaKoti/` directory

### Environment Variables

For AWS scripts, ensure the following environment variables are set:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

### Testing

Run test scripts to verify setup:
```bash
python helloWorld.py  # Should display sync success message
```

---

## Error Handling

### Common Errors

1. **AWS Authentication Errors:**
   - Verify credentials are properly configured
   - Check IAM permissions for S3/EC2 operations

2. **API Connection Errors:**
   - Verify server endpoints are accessible
   - Check network connectivity

3. **Postman Import Errors:**
   - Ensure JSON files are valid
   - Check Postman version compatibility

### Support

For issues or questions:
1. Check error logs in the terminal
2. Verify all prerequisites are installed
3. Ensure proper network connectivity
4. Review AWS IAM permissions

---

## License

This project uses various licenses as specified in individual components:
- Apache 2.0 (OMS Trading API)
- MIT (Pet Store API)

---

*Last updated: December 2024*